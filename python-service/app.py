from http import HTTPStatus
import os
from flask import Flask, Response, request, jsonify
from flask_cors import CORS
from flask_mongoengine import MongoEngine
from utility import check_is_person_sad, get_food_from_csv, recommend
from werkzeug.utils import secure_filename

app = Flask(__name__)
CORS(app)

app.config['MONGODB_SETTINGS'] = {
    'host': os.environ['MONGODB_HOST'],
    'username': os.environ['MONGODB_USERNAME'],
    'password': os.environ['MONGODB_PASSWORD'],
    'db': os.environ['MONGODB_DATABASE']
}

db = MongoEngine()
db.init_app(app)


# # Model class for dataset
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


# GET all recipe name
@app.route("/rest/v1/foods", methods=["GET"])
def handle_search():
    return Response(
        response=Food.objects().to_json(),
        status=HTTPStatus.OK,
        mimetype="application/json"
    )


# Recommend food recipe
@app.route("/rest/v1/recommendation/<id>", methods=["GET"])
def handle_recommendation(id: str):
    food = Food.objects.get(id=id)
    return Response(status=HTTPStatus.NOT_FOUND) if not food else jsonify(recommend(food=food, foods=Food.objects.all()))


@app.route("/rest/v1/upload", methods=["POST"])
def handle_upload():
    VALID_EXTENSION = ["jpg", "png"]
    if request.files['file'].filename == '' or request.files['file'].filename.split(".")[-1] not in VALID_EXTENSION:
        return Response(status=HTTPStatus.BAD_REQUEST)
    else:
        # Create a filename
        filename = secure_filename(request.files['file'].filename)
        # Save file
        request.files['file'].save(filename)
        # Check emotions in image
        response = check_is_person_sad(image=filename)
        # Remove file
        if os.path.exists(filename):
            os.remove(filename)
        return jsonify(response) if response else Response(status=HTTPStatus.INTERNAL_SERVER_ERROR)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
