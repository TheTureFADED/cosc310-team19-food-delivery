from app.repositories.restaurant_repository import (
    restaurant_repo_read_json,
    restaurant_repo_add_restaurant_to_json
)
from app.schemas.restaurant import RestaurantCreate

class DuplicateRestaurantError(Exception):
    pass

def restaurant_service_add(new_restaurant: RestaurantCreate) -> dict:
    restaurants = restaurant_repo_read_json()
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
    return restaurant_repo_add_restaurant_to_json(restaurant)


def restaurant_service_get_all_restaurants() -> list[dict]:
    return restaurant_repo_read_json()

def restaurant_service_get_by_id(restaurant_id: int) -> dict | None:
    restaurants: list[dict] = restaurant_repo_read_json()

    for restaurant in restaurants:
        if restaurant["id"] == restaurant_id:
            return restaurant

    raise KeyError("The restaurant is not in the list.")

def restaurant_service_get_by_cuisine(cuisine: str) -> list[dict] | None:
    return [i for i in restaurant_repo_read_json() 
            if i["cuisine_type"] == cuisine]