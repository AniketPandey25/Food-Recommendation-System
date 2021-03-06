from http import HTTPStatus
import os
import logging
from flask import Flask, Response, request, jsonify
from flask_cors import CORS
from flask_mongoengine import MongoEngine
from utility import check_if_sad, get_food_from_csv, recommend, recommend_for_sad
from werkzeug.utils import secure_filename

app = Flask(__name__)
CORS(app)

# Database configuration
app.config['MONGODB_SETTINGS'] = {
    'host': os.environ['MONGODB_HOST'],
    'username': os.environ['MONGODB_USERNAME'],
    'password': os.environ['MONGODB_PASSWORD'],
    'db': os.environ['MONGODB_DATABASE']
}

# # Initilize database
db = MongoEngine()
db.init_app(app)


# Model class for dataset
class Food(db.Document):
    """
        Document
    """
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


# GET all food
@app.route("/rest/v1/foods", methods=["GET"])
def handle_search():
    return Response(
        response=Food.objects().to_json(),
        status=HTTPStatus.OK,
        mimetype="application/json"
    )


# Recommend food recipe
# If cook time provided will filter out data accordingy
@app.route("/rest/v1/recommendation/<id>", methods=["GET"])
def handle_recommendation(id: str):
    try:
        # Check for query parameter
        cookTime = request.args.get('cookTime')
        # Get the selected food recipe
        food = Food.objects.get(id=id)
        # If invalid food recipe
        if not food:
            return Response(status=HTTPStatus.NOT_FOUND)
        # If cook time given
        if cookTime:
            # Cook time between 20 to 60 inclusive
            if '-' in cookTime:
                [lowerLimit, upperLimit] = map(int, cookTime.split('-'))
                return jsonify(recommend(food=food, foods=Food.objects(cookTime__gte=lowerLimit, cookTime__lte=upperLimit)))
            # Cook time < 20
            elif int(cookTime) == 20:
                return jsonify(recommend(food=food, foods=Food.objects(cookTime__lt=20)))
            # Cook time > 60
            else:
                return jsonify(recommend(food=food, foods=Food.objects(cookTime__gt=60)))
        else:
            return jsonify(recommend(food=food, foods=Food.objects()))
    except Exception as e:
        logging.error(e)
        return Response(status=HTTPStatus.INTERNAL_SERVER_ERROR)


# Handle file upload
# Suggest food on basis of emotion
@app.route("/rest/v1/upload", methods=["POST"])
def handle_upload():
    """
        Suggest food recipe on the basis of mood.
    """
    VALID_EXTENSION = ["jpg", "png"]
    response = None
    if request.files['file'].filename == '' or request.files['file'].filename.split(".")[-1] not in VALID_EXTENSION:
        return Response(status=HTTPStatus.BAD_REQUEST)
    else:
        # Create a filename
        filename = secure_filename(request.files['file'].filename)

        # Save file
        request.files['file'].save(filename)

        # Check emotions in image
        if check_if_sad(image=filename):
            response = recommend_for_sad(foods=Food.objects())

        # Remove file
        if os.path.exists(filename):
            os.remove(filename)

        return jsonify(response) if response else Response(status=HTTPStatus.NO_CONTENT)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
