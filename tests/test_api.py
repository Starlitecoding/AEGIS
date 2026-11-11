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



def test_health_ready():
    response = client.get("/health/ready")
    assert response.status_code == 200
    assert response.json() == {"status": "200"}


def test_create_service():
    response = client.post(
        "/service_add",
        json={
            "name": "test-api",
            "url": "http://127.0.0.1:8001"
        }
    )

    assert response.status_code == 201

    data = response.json()
    assert data["name"] == "test-api"
    assert isinstance(data["service_id"], str)


    