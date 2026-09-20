from fastapi import APIRouter
from app.services.restaurantService import getAllRestaurants

router = APIRouter(prefix="/restaurants")


@router.get("/restaurant-list")
def get_restaurants_list():
    data = getAllRestaurants()
    return data
