from fastapi.testclient import TestClient
import pytest

import json
from pathlib import Path
from app.main import app

from app.services.restaurant_service import restaurant_service_add, restaurant_service_get_all_restaurants, restaurant_service_get_by_id, restaurant_service_get_by_cuisine
from app.schemas.restaurant import RestaurantCreate

DATA = Path("data/restaurants.json")

client = TestClient(app)
@pytest.fixture
def restore_data():
    original = DATA.read_text()
    yield
    DATA.write_text(original)

def restaurant_repo_read_json() -> list[dict]:
    with DATA.open() as file:
        return json.load(file)

sample_restaurant_create = {
    
    "name": "sample_restaurant_create",
    "address": "sample_restaurant_create",
    "phone_number": "sample_restaurant_create",
    "email": "sample_restaurant_create",
    "website": "sample_restaurant_create",
    "cuisine_type": "sample_restaurant_create",
    "opening_hours": "sample_restaurant_create",
    "rating": 0.0
  
}

# """ 
# restaurant_service_add
# restaurant_service_get_all_restaurants
# restaurant_service_get_by_id
# restaurant_service_get_by_cuisine

# """
def test_restaurant_service_get_by_id(restore_data):
    result = restaurant_service_get_by_id(1)
    
    assert isinstance(result, dict)
    assert result["id"] == 1

def test_restaurant_service_get_by_cuisine(restore_data):
    response = restaurant_service_get_by_cuisine("st12ring")
   
    assert isinstance(response, list)
    assert response == [{
    "id": 4,
    "name": "st12ring",
    "address": "stri12ng",
    "phone_number": "s12tring",
    "email": "str12ing",
    "website": "s12tring",
    "cuisine_type": "st12ring",
    "opening_hours": "str12ing",
    "rating": 0.0
  }]


def test_restaurant_service_get_all_restaurants(restore_data):
    response = restaurant_service_get_all_restaurants()
    assert isinstance(response, list)
    assert len(response) == len(restaurant_repo_read_json())

def test_restaurant_service_add(restore_data):
    tmp_len = len(restaurant_repo_read_json())
    new_restaurant = RestaurantCreate(**sample_restaurant_create)
    response = restaurant_service_add(new_restaurant)
    assert isinstance(response, dict)
    assert len(restaurant_repo_read_json()) == tmp_len+1


""" Did not test exceptions  """
    
