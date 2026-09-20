
from app.repositories.restaurantRepository import get_all_restaurants



def get_all_restaurants():
    data: list[dict] = get_all_restaurants()

    return data

def get_restaurant_by_id(restaurant_id: int) -> dict | None:
    restaurants: list[dict] = get_all_restaurants()

    for restaurant in restaurants:
        if restaurant["id"] == restaurant_id:
            return restaurant

    raise KeyError("The restaurant is not in the list.")