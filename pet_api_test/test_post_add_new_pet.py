import requests
import pytest

from pet_api_test.helpers_pet import add_pet

from .test_data import (
    valid_pet,
    invalid_pet_missing_name,
    invalid_pet_invalid_status
)

BASE_URL = "https://petstore.swagger.io/v2/pet"

# ---------------- Helper Function ----------------
def add_pet(pet_data):
    """
    Helper function to add a pet via POST /pet
    Validates test data before sending.
    """

    # ---------------- Validation ----------------
    assert isinstance(pet_data, dict), "Pet data must be a dictionary"

    assert "id" in pet_data, "Pet must have an 'id'"

    assert (
        "category" in pet_data
        and "id" in pet_data["category"]
        and "name" in pet_data["category"]
    ), "Category must have id and name"

    assert (
        "photoUrls" in pet_data
        and isinstance(pet_data["photoUrls"], list)
    ), "photoUrls must be a list"

    assert (
        "tags" in pet_data
        and isinstance(pet_data["tags"], list)
    ), "tags must be a list"

    if "name" in pet_data:
        assert isinstance(
            pet_data["name"], str
        ), "'name' must be a string"

    if "status" in pet_data:
        assert isinstance(
            pet_data["status"], str
        ), "'status' must be a string"

    headers = {
        "Content-Type": "application/json",
        "accept": "application/json"
    }

    response = requests.post(
        BASE_URL,
        json=pet_data,
        headers=headers
    )

    return response


# ---------------- Test Data ----------------
valid_pet = {
    "id": 0,
    "category": {
        "id": 1,
        "name": "Dogs"
    },
    "name": "doggie",
    "photoUrls": ["string"],
    "tags": [
        {
            "id": 1,
            "name": "tag1"
        }
    ],
    "status": "available"
}

invalid_pet_missing_name = {
    "id": 0,
    "category": {
        "id": 1,
        "name": "Dogs"
    },

    # name missing
    "photoUrls": ["string"],

    "tags": [
        {
            "id": 1,
            "name": "tag1"
        }
    ],

    "status": "available"
}

invalid_pet_invalid_status = {
    "id": 0,
    "category": {
        "id": 1,
        "name": "Dogs"
    },

    "name": "doggie",

    "photoUrls": ["string"],

    "tags": [
        {
            "id": 1,
            "name": "tag1"
        }
    ],

    "status": "invalid_status"
}


# ---------------- TEST CASES ----------------

def test_add_valid_pet():
    """
    Add a valid pet should return 200
    """

    response = add_pet(valid_pet)

    # Status code validation
    assert response.status_code == 200

    json_resp = response.json()

    # Response validations
    assert "id" in json_resp
    assert json_resp["name"] == valid_pet["name"]
    assert json_resp["status"] == valid_pet["status"]

    print("Valid pet added successfully")


def test_add_pet_missing_name():
    """
    Add a pet with missing name
    """

    response = add_pet(invalid_pet_missing_name)

    # Petstore API still accepts missing name
    assert response.status_code == 200

    json_resp = response.json()

    # Validate response
    assert "name" not in json_resp or not json_resp["name"]
    assert "id" in json_resp

    print("Pet with missing name tested successfully")


def test_add_pet_invalid_status():
    """
    Add a pet with invalid status
    """

    response = add_pet(invalid_pet_invalid_status)

    # Status code validation
    assert response.status_code == 200

    json_resp = response.json()

    # Response validations
    assert json_resp["status"] == invalid_pet_invalid_status["status"]
    assert json_resp["name"] == invalid_pet_invalid_status["name"]
    assert "id" in json_resp

    print("Pet with invalid status tested successfully")
    