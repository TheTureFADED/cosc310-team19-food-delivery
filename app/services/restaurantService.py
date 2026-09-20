
from app.repositories.restaurantRepository import get_restaurants_json



def get_all_restaurants():
    data: list[dict] = get_restaurants_json()

    return data

def get_restaurant_by_id(restaurant_id: int) -> dict | None:
    restaurants: list[dict] = get_all_restaurants()

    for restaurant in restaurants:
        if restaurant["id"] == restaurant_id:
            return restaurant

    raise KeyError("The restaurant is not in the list.")

def get_restaurants_by_cuisine(cuisine: str) -> list | None:
    return [i for i in get_restaurants_json() if i["cuisine_type"] == cuisine]