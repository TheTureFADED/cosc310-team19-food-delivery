import json
from app.schemas.restaurant import Restaurant


def get_restaurants_json() -> list[dict]:
    with open("data/restaurants.json", "r") as file:
        data: list[dict] = json.load(file)
    return data

def add_restaurant_to_json(restaurant: Restaurant) -> Restaurant:
    restaurants = get_restaurants_json()

    restaurants.append(restaurant)

    with open("data/restaurants.json", "w") as file:
        json.dump(restaurants, file, indent = 2)

    return restaurant
