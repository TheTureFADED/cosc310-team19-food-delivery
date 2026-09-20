import json


def get_all_restaurants():
    with open("data/restaurants.json", "r") as file:
        data = json.load(file)
    return data
