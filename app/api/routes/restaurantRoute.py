from fastapi import APIRouter
from app.services.restaurantService import getAllRestaurants
from app.services.restaurantService import get_restaurant_by_id

router = APIRouter(prefix="/restaurants")


@router.get("/restaurant-list")
def get_restaurants_list():
    data = getAllRestaurants()
    return data

@router.get(
    "/{restaurant_id}"
)
def get(restaurant_id: int):
    return get_restaurant_by_id(restaurant_id)
