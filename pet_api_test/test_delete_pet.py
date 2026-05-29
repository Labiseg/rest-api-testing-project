import requests

from pet_api_test.helpers_pet import delete_pet

BASE_URL = "https://petstore.swagger.io/v2/pet"

# ---------------- Test Data ----------------
pet_id_to_delete = 1

# ---------------- TEST CASE ----------------
def test_delete_pet():

    response = delete_pet(pet_id_to_delete)

    # Validate status code
    assert response.status_code in [200, 404], \
        f"Expected 200 or 404 but got {response.status_code}"

    # Only parse JSON if response has content
    if response.text:

        try:
            response_json = response.json()

            # Validate response structure
            assert "message" in response_json

            print("Response JSON:", response_json)

        except Exception:
            print("Response is not JSON")

    print(f"Delete request executed for pet ID {pet_id_to_delete}")