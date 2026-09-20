import json


def get_all_restaurants():
    with open("data/restaurants.json", "r") as file:
        data: list[dict] = json.load(file)
    return data
