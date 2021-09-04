import csv

DATASET = "dataset.csv"


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
