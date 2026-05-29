import pytest
from .helpers_store import update_store_user


# ---------------- Test Data ----------------
username = "Oreo"

updated_user = {
    "id": 1001,
    "username": "Oreo",
    "firstName": "Mark",
    "lastName": "Labiseg",
    "email": "oreo@example.com",
    "password": "password123",
    "phone": "09123456789",
    "userStatus": 1
}


# ---------------- TEST CASE ----------------
def test_update_store_user():

    # Validation
    assert isinstance(updated_user, dict), \
        "updated_user must be a dictionary"

    assert "username" in updated_user, \
        "username is missing"

    assert "email" in updated_user, \
        "email is missing"

    response = update_store_user(
        username,
        updated_user
    )

    # Status code validation
    assert response.status_code == 200, \
        f"Expected 200 but got {response.status_code}"

    response_json = response.json()

    # Response validation
    assert "code" in response_json
    assert response_json["code"] == 200

    assert "message" in response_json

    print("Store user updated successfully")