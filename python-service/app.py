from http import HTTPStatus
import os
from flask import Flask, Response, request
from flask_mongoengine import MongoEngine
from utility import get_food_from_csv

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'host': os.environ['MONGODB_HOST'],
    'username': os.environ['MONGODB_USERNAME'],
    'password': os.environ['MONGODB_PASSWORD'],
    'db': os.environ['MONGODB_DATABASE']
}

db = MongoEngine()
db.init_app(app)


# Model class for dataset
class Food(db.Document):
    name = db.StringField()
    cookTime = db.IntField()
    cuisine = db.StringField()
    recipe = db.ListField(db.StringField())
    ingredients = db.ListField(db.StringField())
    image = db.StringField()


# This method will execute once when
# the app starts.This will load data
# from the csv file to backend database.
@app.before_first_request
def load_data_into_database():
    for food in get_food_from_csv():
        Food(**food).save()


# Search food recipe from the database
# return five matches
@app.route("/rest/v1/foods", methods=["GET"])
def search():
    recipeName = request.args.get('search')
    return Response(status=HTTPStatus.NO_CONTENT) if recipeName is None or recipeName == '' else Response(response=Food.objects(name__icontains=recipeName)[:5].to_json(), mimetype="application/json", status=HTTPStatus.OK)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
