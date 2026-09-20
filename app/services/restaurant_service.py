
from app.repositories.restaurant_repository import (
    get_restaurants_json,
    add_restaurant_to_json
)
from app.schemas.restaurant import RestaurantCreate


class DuplicateRestaurantError(Exception):
    pass

def create_restaurant(new_restaurant: RestaurantCreate) -> dict:
    restaurants = get_restaurants_json()
    for restaurant in restaurants:
        if restaurant["name"] == new_restaurant.name:
            raise DuplicateRestaurantError(
                "A restaurant with this name already exists"
            )

    next_id: int = max((r["id"] for r in restaurants), default = 0) + 1

    restaurant = {
        "id": next_id,
        **new_restaurant.model_dump()
    }
    return add_restaurant_to_json(restaurant)


def get_all_restaurants() -> list[dict]:
    data: list[dict] = get_restaurants_json()
    return data

def get_restaurant_by_id(restaurant_id: int) -> dict | None:
    restaurants: list[dict] = get_all_restaurants()

    for restaurant in restaurants:
        if restaurant["id"] == restaurant_id:
            return restaurant

    raise KeyError("The restaurant is not in the list.")

def get_restaurants_by_cuisine(cuisine: str) -> list[dict] | None:
    return [i for i in get_restaurants_json() 
            if i["cuisine_type"] == cuisine]