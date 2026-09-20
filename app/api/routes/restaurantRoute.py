from fastapi import APIRouter
from app.services.restaurantService import get_all_restaurants, get_restaurants_by_cuisine
from app.services.restaurantService import get_restaurant_by_id

router = APIRouter(prefix="/restaurants")


@router.get("/restaurant-list")
def get_restaurants_list():
    data = get_all_restaurants()
    return data

@router.get(
    "/{restaurant_id}"
)
def get(restaurant_id: int):
    return get_restaurant_by_id(restaurant_id)

@router.get("")
def list_all(cuisine: str | None = None):
    if cuisine is None:
        return get_all_restaurants()
    return get_restaurants_by_cuisine(cuisine)