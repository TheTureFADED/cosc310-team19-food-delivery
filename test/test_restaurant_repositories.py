import pytest
from app.repositories.restaurant_repository import restaurant_repo_read_json, restaurant_repo_add_restaurant_to_json

import json
from app.schemas.restaurant import Restaurant
from pathlib import Path

DATA = Path("data/restaurants.json")

@pytest.fixture
def restore_data():
    original = DATA.read_text()
    yield
    DATA.write_text(original)

sample_restaurant_add_in_repo = {
    "id":1000,
    "name": "sample_restaurant_add_in_repo",
    "address": "sample_restaurant_add_in_repo",
    "phone_number": "sample_restaurant_add_in_repo",
    "email": "sample_restaurant_add_in_repo",
    "website": "sample_restaurant_add_in_repo",
    "cuisine_type": "sample_restaurant_add_in_repo",
    "opening_hours": "sample_restaurant_add_in_repo",
    "rating": 0.0
  
}

@pytest.mark.skip(reason="not implemented yet")
def test_delete_operation(restore_data):
    assert False
# @pytest.mark.skip(reason="not implemented yet")
def test_new_add_operation(restore_data):
    length_before_add = len(restaurant_repo_read_json())
    # restaurant = Restaurant(**sample_restaurant_add_in_repo)
    restaurant = sample_restaurant_add_in_repo
    new_added_restaurant = restaurant_repo_add_restaurant_to_json(restaurant)
    length_after_add = len(restaurant_repo_read_json())

    assert isinstance(new_added_restaurant, dict)
    assert length_after_add > length_before_add

# @pytest.mark.skip(reason="not implemented yet")
def test_get_all_restaurants(restore_data):
    cap = restaurant_repo_read_json()
    assert isinstance(cap, list)
    assert len(cap) > 0 