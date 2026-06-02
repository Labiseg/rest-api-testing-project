import requests

# ---------------- BASE URL ----------------
BASE_URL = "https://petstore.swagger.io/v2/user"

# ---------------- TEST DATA ----------------
username = "oreo"
password = "1213"

# ---------------- TEST CASE ----------------
def test_user_login():

    response = requests.get(
        f"{BASE_URL}/login",
        params={
            "username": username,
            "password": password
        }
    )

    # Validate status code
    assert response.status_code in [200, 400], \
        f"Expected 200 or 400 but got {response.status_code}"

    # Only parse JSON if response has content
    if response.text:

        try:
            response_json = response.json()

            # ---------------- SUCCESS CASE ----------------
            if response.status_code == 200:

                # Validate required fields
                assert "code" in response_json
                assert "type" in response_json
                assert "message" in response_json

                # Validate values
                assert response_json["code"] == 200
                assert response_json["type"] == "unknown"

                assert "logged in user session" in response_json["message"]

                print("Login Success Response:", response_json)

            # ---------------- ERROR CASE ----------------
            elif response.status_code == 400:

                assert "code" in response_json
                assert "type" in response_json
                assert "message" in response_json

                assert response_json["code"] == 400
                assert response_json["type"] == "error"

                print("Login Failed Response:", response_json)

        except Exception:
            assert False, "Response is not valid JSON"

    print(f"Login request executed for username '{username}'")