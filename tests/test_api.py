from fastapi.testclient import TestClient
from config import url_list
import main

client = TestClient(main.app)

def test_response_root():
    response = client.get("/")
    assert response.status_code == 200


def test_health_live():
    response = client.get("/health/live")
    assert response.status_code == 200
    assert response.json() == {"status": "api alive"}    


def test_services():
    response = client.get("/services")
    assert response.status_code == 200
    assert  response.json() == url_list


def test_health_ready():
    response = client.get("/health/ready")
    assert response.status_code == 200
    assert response.json() == {"status": "200"}