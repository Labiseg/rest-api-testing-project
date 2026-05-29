import pytest
from .helpers_store import delete_store_user


# ---------------- Test Data ----------------
username = "Oreo"


# ---------------- TEST CASE ----------------
def test_delete_store_user():

    # Validation
    assert isinstance(username, str), \
        "Username must be a string"

    response = delete_store_user(username)

    # Validate allowed responses
    assert response.status_code in [200, 404], \
        f"Unexpected status code: {response.status_code}"

    # If user exists and deleted successfully
    if response.status_code == 200:

        response_json = response.json()

        assert "code" in response_json
        assert response_json["code"] == 200

        assert "message" in response_json

        print(f"User '{username}' deleted successfully")

    # If user does not exist
    elif response.status_code == 404:

        print(f"User '{username}' not found as expected")
        