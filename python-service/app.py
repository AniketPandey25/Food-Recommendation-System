import os
from flask import Flask, Response
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


class Food(db.Document):
    name = db.StringField()
    cookTime = db.IntField()
    cuisine = db.StringField()
    ingredients = db.ListField(db.StringField())
    image = db.StringField()


@app.route("/api/v1/foods")
def get_recommendation():
    for food in get_food_from_csv()[:5]:
        Food(**food).save()
    return Response(Food.objects().to_json(), mimetype="application/json", status=200)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
