import json
import shutil
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from app.main import app

DATA = Path("data")

def restaurant_repo_list() -> list[dict]:
    with DATA.open() as file:
        return json.load(file)

@pytest.fixture(autouse = True)
def isolated_data(tmp_path, monkeypatch):
    for name in ("restaurants.json",):
        shutil.copy(DATA / name, tmp_path / name)
    monkeypatch.setenv("COSC310_DATA_DIR", str(tmp_path))

@pytest.fixture
def client():
    return TestClient(app)