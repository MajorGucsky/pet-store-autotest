import pytest

from utils.api_client import ApiClient

BASE_URL = "https://petstore.swagger.io/v2"
pet_name = "Stepan"
pet_id = 26


@pytest.fixture
def api_client():
    return ApiClient(BASE_URL)


def test_create_pet(api_client):
    data = {
            "id": pet_id,
            "name": "pet_name",
            "photoUrls": ["http://example.com/photo.jpg"],
            "status": "available"
    }
    response = api_client.post("/pet", data=data)

    assert response.status_code == 200
    assert response.json()["name"] == "pet_name"

def test_get_pet(api_client):
    response = api_client.get(f"/pet/{pet_id}")
    assert response.status_code == 200
    assert response.json()["id"] == pet_id