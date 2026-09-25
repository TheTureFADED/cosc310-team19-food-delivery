from fastapi import APIRouter, FastAPI, HTTPException, status
from app.services import restaurant_service
from app.services.restaurant_service import (
    restaurant_service_create,
    restaurant_service_list,
    restaurant_service_get_by_cuisine,
    restaurant_service_get_by_id,
    restaurant_service_delete,
    DuplicateRestaurantError,
    RestaurantNotFoundError
)

from app.schemas.restaurant import RestaurantCreate, RestaurantRead, RestaurantUpdate

router = APIRouter(prefix="/restaurants")
all_restaurant = restaurant_service_list()

@router.get(
        "",
        status_code = status.HTTP_200_OK)
def restaurant_route_get_list() -> list[dict]:
    return all_restaurant;

@router.get(
        "/{restaurant_id}",
        response_model = RestaurantCreate,  
        # filters anything not declared in the model of RestaurantCreate
        status_code = status.HTTP_200_OK) 
def restaurant_route_get_by_id(restaurant_id: int) -> dict:
    try: 
        return restaurant_service_get_by_id(restaurant_id)

    except RestaurantNotFoundError as e:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = str(e)
        )

@router.get(
        "/filtered-by-cuisine-type",
        response_model = RestaurantRead,
        status_code = status.HTTP_200_OK)
def restaurant_route_get_by_cuisine(cuisine: str | None = None) -> list[dict]:
    try:
        if cuisine is None:
            return all_restaurant
        return restaurant_service_get_by_cuisine(cuisine)
    except RestaurantNotFoundError as e:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = str(e)
        )

@router.post( 
        "", 
        status_code=status.HTTP_201_CREATED)
def restaurant_route_create(new_restaurant: RestaurantCreate) -> dict:
    try:
        return restaurant_service_create(new_restaurant)

    except DuplicateRestaurantError as e:
        raise HTTPException(
            status_code = status.HTTP_409_CONFLICT,
            detail = str(e)
        )

@router.delete(
        "/{restaurant_id}",
        status_code = status.HTTP_204_NO_CONTENT
        )
def restaurant_route_delete(restaurant_id: int) -> None:
    try:
        return restaurant_service_delete(restaurant_id)

    except RestaurantNotFoundError as e:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = str(e)
        )