import requests

# ---------------- BASE URL ----------------
BASE_URL = "https://petstore.swagger.io/v2/user"

# ---------------- TEST DATA ----------------
payload = [
    {
        "id": 101,
        "username": "oreo",
        "firstName": "Mark",
        "lastName": "Labiseg",
        "email": "oreo@example.com",
        "password": "1213",
        "phone": "09123456789",
        "userStatus": 1
    }
]

# ---------------- TEST CASE ----------------
def test_create_user_with_array():

    response = requests.post(
        f"{BASE_URL}/createWithArray",
        json=payload,
        headers={"Content-Type": "application/json"}
    )

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

            print("Create With Array Response:", response_json)

        except Exception:
            assert False, "Response is not valid JSON"

    print("CreateWithArray request executed successfully")
    