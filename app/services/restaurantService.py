
from app.repositories.restaurantRepository import get_all_restaurants



def getAllRestaurants():
    data: list[dict] = get_all_restaurants()

    return data