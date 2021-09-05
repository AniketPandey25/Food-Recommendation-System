import csv
from difflib import SequenceMatcher

DATASET = "dataset.csv"


# Match percentage for two string
def percentage_match(string1, string2):
    return SequenceMatcher(isjunk=None, a=string1, b=string2).ratio()


def join_ingredients(ingredients):
    return " ".join(ingredients)


# Recommend food recipe
def recommend(food, foods):
    return [
        f for f in foods if percentage_match(food.name, f.name) >= 0.6 and percentage_match(join_ingredients(food.ingredients), join_ingredients(f.ingredients)) >= 0.5
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
