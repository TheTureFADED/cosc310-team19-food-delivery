from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)



def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Backend is running"}



def test_health_status_good():
    response = client.get("/health")
    
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
    

def test_unknown_route_returns_404():
    bad_response = client.get("/anythinganything")
    assert bad_response.status_code == 404


    
