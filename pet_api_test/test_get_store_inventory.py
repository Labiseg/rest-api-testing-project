import pytest
from .helpers_store import get_store_inventory


# ---------------- TEST CASE ----------------
def test_get_store_inventory():

    response = get_store_inventory()

    # Validate status code
    assert response.status_code == 200, \
        f"Expected 200 but got {response.status_code}"

    # Convert response to JSON
    response_json = response.json()

    # Validate response type
    assert isinstance(response_json, dict), \
        "Response should be a dictionary"

    # Validate inventory values
    for status, quantity in response_json.items():

        assert isinstance(status, str), \
            "Status should be a string"

        assert isinstance(quantity, int), \
            f"Quantity for {status} should be integer"

    print("Store inventory retrieved successfully")