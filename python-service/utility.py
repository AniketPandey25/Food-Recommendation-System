import os
import csv
import boto3
import random
import logging
from botocore.exceptions import ClientError
from difflib import SequenceMatcher

DATASET = "dataset.csv"


def get_client():
    """
        Create low-level service client by name.
    """
    return boto3.client(
        service_name="rekognition",
        region_name="ap-south-1",
        aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
        aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY']
    )


def get_faces_from_image(image):
    """
        AWS Rekognition

        :type image: File
        :param image: Image

        :return Any
    """
    with open(file=image, mode='rb') as image:
        return get_client().detect_faces(
            Image={
                "Bytes": image.read()
            }, Attributes=["ALL"]
        )["FaceDetails"]


def get_emotions(image):
    """
        Retrieve emotion from image

        :type image: File
        :param image: Image

        :return list
    """
    try:
        for face in get_faces_from_image(image=image):
            return face['Emotions']
    except (ClientError, Exception) as e:
        logging.error(e)
        return None


def check_if_sad(image):
    """
        Check if found SAD or ANGRY or FEARFUL

        :type image: File
        :param image: Image

        :return bool
    """
    emotion = get_emotions(image=image)
    return emotion[0]['Type'] in ['SAD', 'ANGRY', 'FEAR'] if emotion else False


def percentage_match(string1, string2):
    """
        Get percentage match between two strings

        :return float
    """
    return SequenceMatcher(isjunk=None, a=string1, b=string2).ratio()


def join_ingredients(ingredients):
    """
        Join each element present in the list by \s
        to create a string

        :type ingredients: list
        :param ingredients: List of ingredients

        :return str
    """
    return " ".join(ingredients)


def recommend(food, foods):
    """
        Get recommendation

        :type food: Food
        :param food: Food recipe selected

        :type foods: [Food]
        :param foods: All availabe food recipe

        :return dict[str, list] 
    """
    return {
        "foods": [f for f in foods if percentage_match(food.name, f.name) >= 0.2 and
                  percentage_match(join_ingredients(
                      food.ingredients), join_ingredients(f.ingredients)) >= 0.5
                  ][:9],
        "majorIngredients": get_major_ingredients(food.ingredients)
    }


def check_food_edible_when_sad(food):
    """
        Check if food recipe edible when feeling sad.

        :type food: Food
        :param food: Food object

        :return bool
    """
    ingredients_to_take_when_sad = [
        "chocolate",
        "fish",
        "avacado"
        "yogurt",
        "orange",
        "spinach",
        "brazil nuts",
        "beans",
        "peas",
        "berries",
        "almonds",
        "brocoli"
    ]
    for ingredient_to_take_when_sad in ingredients_to_take_when_sad:
        return any(
            [
                True for ingredient in food.ingredients if ingredient_to_take_when_sad in ingredient.lower()
            ]
        )
    return False


def recommend_for_sad(foods):
    """
        Recommend food recipe for feeling SAD

        :type foods: List[Food]
        :param foods: Collection Food

        :return list[Food]
    """
    return random.sample(population=[food for food in foods if check_food_edible_when_sad(food)], k=5)


def get_major_ingredients(ingredients):
    """
        Get major ingredients

        This method will remove all the minor ingredients
        like salt, sugar etc

        :return list
    """
    minor_ingredients = ["seed", "salt", "sugar", "powder", "oil"]
    major_ingredients = []
    for ingredient in ingredients:
        if not any([True for minor_ingredient in minor_ingredients if minor_ingredient in ingredient]):
            major_ingredients.append(ingredient)
    return major_ingredients


def get_dict(row):
    """
        Get dict from csv row

        :type row: list
        :param row: All fields from csv

        :return dict[str, Any]
    """
    return {
        "name": row[0],
        "cookTime": row[2],
        "cuisine": row[3],
        "recipe": row[4].split("\n"),
        "ingredients": row[6].split(","),
        "image": row[7]
    }


def get_food_from_csv():
    """
        Get data from dataset

        :return list
    """
    data = []
    with open(DATASET, 'r') as file:
        csvReader = csv.reader(file)
        next(csvReader)  # Skipping the first row
        for row in csvReader:
            data.append(get_dict(row))
    return data
