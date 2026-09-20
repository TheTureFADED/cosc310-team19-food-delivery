import json
from app.schemas.restaurant import Restaurant
from pathlib import Path

DATA = Path("app/data/restaurants.json")


def restaurant_repo_read_json() -> list[dict]:
    with DATA.open() as file:
        return json.load(file)

def restaurant_repo_add_restaurant_to_json(restaurant: Restaurant) -> Restaurant:
    restaurants: list[dict] = restaurant_repo_read_json()

    restaurants.append(restaurant)

    with DATA.open("w") as file:
        json.dump(restaurants, file, indent = 2)

    return restaurant
