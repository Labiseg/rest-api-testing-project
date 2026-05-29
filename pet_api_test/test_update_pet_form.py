
import requests
import pytest

from pet_api_test.helpers_pet import create_pet, get_pet_by_id

BASE_URL = "https://petstore.swagger.io/v2/pet"


# ---------------- TEST CASE ----------------
def test_update_pet_form_data():

    # ---------------- CREATE PET FIRST ----------------
    create_response = create_pet()

    assert create_response.status_code == 200, \
        f"Pet creation failed with {create_response.status_code}"

    # ---------------- UPDATE PET ----------------
    pet_id = 2001

    payload = {
        "name": "oreo",
        "status": "available"
    }

    update_response = requests.post(
        f"{BASE_URL}/{pet_id}",
        data=payload,
        headers={
            "Content-Type": "application/x-www-form-urlencoded",
            "accept": "application/json"
        }
    )

    # ---------------- VALIDATE UPDATE RESPONSE ----------------
    assert update_response.status_code == 200, \
        f"Expected 200 but got {update_response.status_code}"

    # ---------------- VERIFY UPDATED PET ----------------
    get_response = get_pet_by_id(pet_id)

    assert get_response.status_code == 200

    get_json = get_response.json()

    # ---------------- VALIDATIONS ----------------
    assert get_json["id"] == pet_id
    assert get_json["name"] == "oreo"
    assert get_json["status"] == "available"

    print("Pet updated successfully")
    