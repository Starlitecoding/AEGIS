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


# def test_services():
#     response = client.get("/service_list")
#     assert response.status_code == 200

#     urls = [service["url"] for service in response.json()]
#     expected_urls = [service["url"] for service in main.list_services]

#     assert urls == expected_urls


def test_health_ready():
    response = client.get("/health/ready")
    assert response.status_code == 200
    assert response.json() == {"status": "200"}


def test_create_service():
    response = client.post("/service_add")
    assert response.status_code == 201
    assert isinstance(response.json()["service_id"], str)
    assert isinstance(response.json()["url"], str)
    assert isinstance(response.json()["name"], str)
    
def test_duplicate_service():
    response = client.post("/service_add")
    assert response.status_code == 409
    
    
# def test_delete_unknown():
#     response = client.delete("/service_delete")
#     assert response.status_code == 404
    
# def test_delete_service():
#     response = client.delete("/service_delete/{item_id}")
#     assert response.status_code == 200
#     assert response.json == {"message": f"Service {i['name']} removed"}
    
# def test_health_services():
#     response = client.get("/health/services")
    