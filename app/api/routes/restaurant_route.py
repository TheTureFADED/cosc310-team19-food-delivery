from fastapi import APIRouter, FastAPI, HTTPException, status
from app.services import restaurant_service
from app.services.restaurant_service import (
    restaurant_service_add,
    restaurant_service_get_all_restaurants,
    restaurant_service_get_by_cuisine,
    restaurant_service_get_by_id,
    DuplicateRestaurantError
)

from app.schemas.restaurant import RestaurantCreate



router = APIRouter(prefix="/restaurants")

@router.get("/restaurant-list")
def get_restaurants_list() -> list[dict]:
    return restaurant_service_get_all_restaurants();

@router.get("/{restaurant_id}") 
def get(restaurant_id: int) -> dict:
    return restaurant_service_get_by_id(restaurant_id)

@router.get("")
def list_all(cuisine: str | None = None) -> list[dict]:
    if cuisine is None:
        return restaurant_service_get_all_restaurants()
    return restaurant_service_get_by_cuisine(cuisine)

@router.post(
        "/restaurant-list", 
        status_code=status.HTTP_201_CREATED)
def add_restaurant(new_restaurant: RestaurantCreate) -> dict:
    try:
        return restaurant_service_add(new_restaurant)

    except DuplicateRestaurantError as e:
        raise HTTPException(
            status_code = status.HTTP_409_CONFLICT,
            detail = str(e)
        )