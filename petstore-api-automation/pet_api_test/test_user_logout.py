import requests

# ---------------- BASE URL ----------------
BASE_URL = "https://petstore.swagger.io/v2/user"

# ---------------- TEST CASE ----------------
def test_user_logout():

    response = requests.get(f"{BASE_URL}/logout")

    # Validate status code
    assert response.status_code == 200, \
        f"Expected 200 but got {response.status_code}"

    # Only parse JSON if response has content
    if response.text:

        try:
            response_json = response.json()

            # ---------------- VALIDATION ----------------
            assert "code" in response_json
            assert "type" in response_json
            assert "message" in response_json

            # Validate values
            assert response_json["code"] == 200
            assert response_json["type"] == "unknown"
            assert response_json["message"] == "ok"

            print("Logout Response:", response_json)

        except Exception:
            assert False, "Response is not valid JSON"

    print("Logout request executed successfully")