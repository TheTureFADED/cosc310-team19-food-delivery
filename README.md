# COSC 310 Team 19 Food Delivery

This is our team project for COSC 310. The goal is to build a food delivery app that satisfies common food delivery app functions, where customers can find restaurants, view menus, place orders, and follow their deliveries. Right now, the `main` branch has a basic FastAPI backend for listing and adding restaurants. The other food delivery features are planned but are not implemented in this branch yet.

## What works right now

- Get the list of restaurants.
- Get one restaurant by its ID.
- Filter restaurants by `cuisine_type` using an exact match.
- Add a restaurant. The app assigns it the next numeric ID and saves it to `data/restaurants.json`.
- Reject a new restaurant and produces 409 CONFLICT if another restaurant already has the same name.
- Check that the server is running with `/` or `/health`.

## Set up the backend

Python and Git is required. Run these commands from the project root (the folder containing `requirements.txt` and `data/`).

```bash
git clone https://github.com/TheTureFADED/cosc310-team19-food-delivery
cd cosc310-team19-food-delivery
python -m venv .venv
```

Activate the virtual environment:

```bash
# Windows PowerShell
.venv\Scripts\Activate.ps1

# macOS or Linux
source .venv/bin/activate
```

## Dependency Installation
Run the next commands in the same terminal:

```bash
python -m pip install -r requirements.txt
python -m uvicorn app.main:app --reload
```

Open `http://127.0.0.1:8000/docs` to try the API in your browser. The app runs at `http://127.0.0.1:8000`. Stop it with `Ctrl+C`.

If `python` is not the command for Python on your computer, use `python3` (on mac) in the commands above.

## Current API

| Method | Path | What it does |
| --- | --- | --- |
| `GET` | `/` | Returns a message that the backend is running. |
| `GET` | `/health` | Returns `{"status": "ok"}`. |
| `GET` | `/restaurants` | Returns all restaurants. |
| `GET` | `/restaurants?cuisine=xxx` | Returns restaurants whose `cuisine_type` is exactly `xxx`. |
| `GET` | `/restaurants/restaurant-list` | Also returns all restaurants. |
| `GET` | `/restaurants/{restaurant_id}` | Returns a restaurant by numeric ID. |
| `POST` | `/restaurants/restaurant-list` | Adds a restaurant and returns it with a new ID. |

To add a restaurant, open `/docs`, find `POST /restaurants/restaurant-list`, and select **Try it out**. The request body needs these fields:

```json
{
  "name": "Example Kitchen",
  "address": "123 Example Street, Kelowna, BC",
  "phone_number": "123-456-7890",
  "email": "hello@example.com",
  "website": "https://example.com",
  "cuisine_type": "Italian",
  "opening_hours": "Mon-Sun: 11:00 AM - 9:00 PM",
  "rating": 4.5
}
```

The POST route returns HTTP `201` when a restaurant is added and HTTP `409` if the same name already exists. 

## Project folders

| Path | Purpose |
| --- | --- |
| `app/main.py` | Starts the FastAPI app and includes the restaurant routes. |
| `app/api/routes/restaurant_route.py` | Handles restaurant HTTP requests. |
| `app/schemas/restaurant.py` | Defines the restaurant request and data fields. |
| `app/services/restaurant_service.py` | Handles restaurant rules, including duplicate names and new IDs. |
| `app/repositories/restaurant_repository.py` | Reads and writes restaurant data. |
| `data/restaurants.json` | Stores the restaurant list. |
| `requirements.txt` | Lists the Python packages needed to run the backend. |

## Location of representative data

The restaurant request goes from the route to the service, then to the repository, which reads or updates the JSON file. To prevent any misuse or meddling with original data, the repository uses the relative path `data/restaurants.json`.
