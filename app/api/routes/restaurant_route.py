from fastapi import APIRouter, HTTPException, status
from app.services.restaurant_service import (
    get_all_restaurants, 
    get_restaurants_by_cuisine,
    get_restaurant_by_id,
    create_restaurant,
    DuplicateRestaurantError
)
from app.schemas.restaurant import RestaurantCreate

router = APIRouter(prefix="/restaurants")


@router.get("/restaurant-list")
def get_restaurants_list() -> list[dict]:
    data = get_all_restaurants()
    return data

@router.get("/{restaurant_id}") 
def get(restaurant_id: int) -> dict:
    return get_restaurant_by_id(restaurant_id)

@router.get("")
def list_all(cuisine: str | None = None) -> list[dict]:
    if cuisine is None:
        return get_all_restaurants()
    return get_restaurants_by_cuisine(cuisine)

@router.post("", status_code=status.HTTP_201_CREATED)
def create(new_restaurant: RestaurantCreate) -> dict:
    try:
        return create_restaurant(new_restaurant)

    except DuplicateRestaurantError as e:
        raise HTTPException(
            status_code = status.HTTP_409_CONFLICT,
            detail = str(e)
        )