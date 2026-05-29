import requests
import pytest

from .helpers_pet import (
    add_pet,
    get_pet,
    delete_pet
)

from .test_data import (
    valid_pet,
    invalid_pet_missing_name,
    invalid_pet_invalid_status
)
from .test_data import valid_pet, invalid_pet_missing_name, invalid_pet_invalid_status

BASE_URL = "https://petstore.swagger.io/v2/pet"

# ---------------- TEST CASES ----------------
@pytest.mark.parametrize("pet,description", [
    (valid_pet, "Valid Pet"),
    (invalid_pet_missing_name, "Pet Missing Name"),
    (invalid_pet_invalid_status, "Pet Invalid Status")
])
def test_add_and_get_pet(pet, description):
    # Add pet
    post_resp = add_pet(pet)
    assert post_resp.status_code == 200
    post_json = post_resp.json()
    pet_id = post_json.get("id")
    assert pet_id is not None, f"{description}: Pet ID not returned"

    # GET pet to confirm it exists
    get_resp = get_pet(pet_id)
    assert get_resp.status_code == 200
    get_json = get_resp.json()
    if "name" in pet:
        assert get_json["name"] == pet.get("name")
    if "status" in pet:
        assert get_json["status"] == pet.get("status")

    print(f"{description}: POST + GET successful for Pet ID {pet_id}")

    # Clean up: delete pet after test
    del_resp = delete_pet(pet_id)
    assert del_resp.status_code == 200 or del_resp.status_code == 404  # 404 if already deleted