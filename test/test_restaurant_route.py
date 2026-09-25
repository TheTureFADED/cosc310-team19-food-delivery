from fastapi.testclient import TestClient
import pytest
from fastapi import APIRouter, FastAPI, HTTPException, status
import json
from pathlib import Path
from app.main import app
from pydantic import BaseModel
DATA = Path("data/restaurants.json")

def restaurant_repo_list() -> list[dict]:
    with DATA.open() as file:
        return json.load(file)

client = TestClient(app)
@pytest.fixture
def restore_data():
    original = DATA.read_text()
    yield
    DATA.write_text(original)


def test_get_restaurants_list():
    
    response = client.get("/restaurants")
    print(response.json() == restaurant_repo_list())
    assert response.status_code == 200
    assert response.json() == restaurant_repo_list()

def test_get_restaurants_by_id():
    response = client.get("/restaurants/1")
    assert response.status_code == 200
    response = response.json()
    assert response["id"] == 1

def test_get_by_cuisine():
    response = client.get("/restaurants/filtered-by-Italian-type")
    assert response.status_code == 200
    response = response.json()
    assert response == [{
    "id": 2,
    "name": "Cedar & Co.",
    "address": "45 Oak Avenue, Burnaby, BC",
    "phone_number": "604-555-0102",
    "email": "contact@cedarco.ca",
    "website": "https://cedarco.ca",
    "cuisine_type": "Italian",
    "opening_hours": "Tue-Sun: 11:30 AM - 10:00 PM",
    "rating": 4.5,
    "availability": True
  }]



def test_add_new_restaurants_created():
    response = client.post(
        "/restaurants", 
        json =  {
            "id":6,
            "name":"testRestaurant",
            "address":"testAddress",
            "phone_number":"testPhone",
            "email":"testEmail",
            "website":"testWebsite",
            "cuisine_type":"testCuisine",
            "opening_hours":"testHours",
            "rating":5.0,
            "availability": True
        }
    )
    
    assert response.status_code == 201
    

def test_add_new_restaurants_conflict():

    client.post(
        "/restaurants", 
        json = {
            "id":6,
            "name":"testRestaurant",
            "address":"testAddress",
            "phone_number":"testPhone",
            "email":"testEmail",
            "website":"testWebsite",
            "cuisine_type":"testCuisine",
            "opening_hours":"testHours",
            "rating":5.0,
            "availability": True
        }
    )
    
    response = client.post(
        "/restaurants/restaurant-list", 
        json =  {
            "id":6,
            "name":"testRestaurant",
            "address":"testAddress",
            "phone_number":"testPhone",
            "email":"testEmail",
            "website":"testWebsite",
            "cuisine_type":"testCuisine",
            "opening_hours":"testHours",
            "rating":5.0,
            "availability": True
        }
    )
    
    assert response.status_code == 409
    
    
    