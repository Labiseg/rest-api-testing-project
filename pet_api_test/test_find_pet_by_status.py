import requests
import pytest

from pet_api_test.helpers_pet import get_pet_by_status

BASE_URL = "https://petstore.swagger.io/v2/pet/findByStatus"

# ---------------- Test Data ----------------
valid_statuses = ["available", "pending", "sold"]
invalid_status = "invalid_status"


# ---------------- TEST CASES ----------------

@pytest.mark.parametrize("status", valid_statuses)
def test_find_pet_by_valid_status(status):

    response = get_pet_by_status(status)

    # Validate status code
    assert response.status_code == 200

    response_json = response.json()

    # Validate response is a list
    assert isinstance(response_json, list)

    # Validate returned pets contain requested status
    if len(response_json) > 0:
        assert response_json[0]["status"] == status

    print(f"Pets with status '{status}' retrieved successfully")


def test_find_pet_by_invalid_status():

    response = get_pet_by_status(invalid_status)

    # Swagger Petstore may return 400 or 200
    assert response.status_code in [200, 400]

    print("Invalid status test executed successfully")