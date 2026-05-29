import requests

BASE_URL = "https://petstore.swagger.io/v2/pet"

def test_update_existing_pet():

    payload = {
        "id": 1010,
        "category": {
            "id": 1,
            "name": "Dogs"
        },
        "name": "Buddy Updated",
        "photoUrls": [
            "https://example.com/dog.jpg"
        ],
        "tags": [
            {
                "id": 1,
                "name": "friendly"
            }
        ],
        "status": "available"
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.put(
        BASE_URL,
        json=payload,
        headers=headers
    )

    # Status code validation
    assert response.status_code == 200

    response_json = response.json()

    # Response validations
    assert response_json["id"] == 1010
    assert response_json["name"] == "Buddy Updated"
    assert response_json["status"] == "available"
    assert response_json["category"]["name"] == "Dogs"

    print("Pet updated successfully")