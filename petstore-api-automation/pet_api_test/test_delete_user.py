import requests

# ---------------- BASE URL ----------------
BASE_URL = "https://petstore.swagger.io/v2/user"

# ---------------- TEST DATA ----------------
username = "oreo"

# ---------------- TEST CASE ----------------
def test_delete_user():

    response = requests.delete(f"{BASE_URL}/{username}")

    # Validate status code
    assert response.status_code in [200, 400, 404], \
        f"Expected 200, 400, or 404 but got {response.status_code}"

    # Only parse JSON if response has content
    if response.text:

        try:
            response_json = response.json()

            # ---------------- SUCCESS CASE ----------------
            if response.status_code == 200:

                assert "code" in response_json
                assert "type" in response_json
                assert "message" in response_json

                assert response_json["code"] == 200
                assert response_json["type"] == "unknown"

                # message should return deleted username
                assert response_json["message"] == username

                print("Delete Success Response:", response_json)

            # ---------------- ERROR CASE ----------------
            elif response.status_code == 404:

                assert response_json["code"] == 1
                assert response_json["type"] == "error"
                assert response_json["message"] == "User not found"

                print("User Not Found:", response_json)

            elif response.status_code == 400:

                assert response_json["code"] == 400
                assert "message" in response_json

                print("Invalid Username:", response_json)

        except Exception:
            assert False, "Response is not valid JSON"

    print(f"DELETE request executed for username '{username}'")