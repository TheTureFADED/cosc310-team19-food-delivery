import json


def get_restaurants_json():
    with open("data/restaurants.json", "r") as file:
        data: list[dict] = json.load(file)
    return data
