import os
import csv
import boto3
import logging
from botocore.exceptions import ClientError
from difflib import SequenceMatcher

DATASET = "dataset.csv"


# Get client
def get_client():
    return boto3.client(
        service_name="rekognition",
        region_name="ap-south-1",
        aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
        aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY']
    )


# Use AWS Rekognition to find out emotion
# for an image
def get_faces_from_image(image):
    with open(file=image, mode='rb') as image:
        return get_client().detect_faces(
            Image={
                "Bytes": image.read()
            }, Attributes=["ALL"]
        )["FaceDetails"]


# Check is person Sad
def check_is_person_sad(image):
    try:
        for face in get_faces_from_image(image=image):
            return face['Emotions']
    except (ClientError, Exception) as e:
        logging.error(e)
        return None


# Match percentage for two string
def percentage_match(string1, string2):
    return SequenceMatcher(isjunk=None, a=string1, b=string2).ratio()


def join_ingredients(ingredients):
    return " ".join(ingredients)


# Recommend food recipe
def recommend(food, foods):
    return [
        f for f in foods if percentage_match(food.name, f.name) >= 0.2 and percentage_match(join_ingredients(food.ingredients), join_ingredients(f.ingredients)) >= 0.4
    ][:5]


# Restructure data
def get_dict(row):
    return {
        "name": row[0],
        "cookTime": row[2],
        "cuisine": row[3],
        "recipe": row[4].split("\n"),
        "ingredients": row[6].split(","),
        "image": row[7]
    }


# Load data from csv
def get_food_from_csv():
    data = []
    with open(DATASET, 'r') as file:
        csvReader = csv.reader(file)
        next(csvReader)  # Skipping the first row
        for row in csvReader:
            data.append(get_dict(row))
    return data
