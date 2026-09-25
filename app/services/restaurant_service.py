from app.repositories.restaurant_repository import (
    restaurant_repo_read_json,
    restaurant_repo_add_restaurant_to_json
)
from app.schemas.restaurant import Restaurant, RestaurantCreate
from app.errors import DuplicateRestaurantError, RestaurantNotFoundError

def restaurant_service_create(new_restaurant: RestaurantCreate) -> Restaurant:
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


def restaurant_service_list() -> list[Restaurant]:
    restaurants = restaurant_repo_read_json()
    return [Restaurant(**restaurant) for restaurant in restaurants]

def restaurant_service_get_by_id(restaurant_id: int) -> Restaurant:
    restaurants: list[dict] = restaurant_repo_read_json()

    for restaurant in restaurants:
        if restaurant["id"] == restaurant_id:
            return Restaurant(**restaurant)

    raise RestaurantNotFoundError(
        f"Restaurant with id {restaurant_id} was not found."
    )

def restaurant_service_get_by_cuisine(cuisine: str) -> list[Restaurant]:
    restaurants = restaurant_repo_read_json()

    return [
        Restaurant(**restaurant)
        for restaurant in restaurants
        if restaurant["cuisine_type"].lower() == cuisine.lower()
    ]

def restaurant_service_delete(restaurant_id: int) -> None:
