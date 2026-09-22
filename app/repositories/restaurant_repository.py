import json
from pathlib import Path
class RestaurantRepository:
    def __init__(self, data_path: str = "data/restaurants.json"):
        self.data_path = Path(data_path)

    def _load(self) -> list[dict]:
        if not self.data_path.exists():
            return []
        with open(self.data_path, "r", encoding="utf-8") as f:
            return json.load(f)

    def get_all(self) -> list[dict]:
        return self._load()

    def get_by_id(self, restaurant_id: int) -> dict | None:
        for restaurant in self._load():
            if restaurant["id"] == restaurant_id:
                return restaurant
        return None