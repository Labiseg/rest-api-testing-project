import requests

BASE_URL = "https://petstore.swagger.io/v2/user"
username = "Oreo"

def test_get_user():

    response = requests.get(f"{BASE_URL}/{username}")

    assert response.status_code in [200, 404]

    response_json = response.json()

    if response.status_code == 200:
        assert response_json["username"] == username

    elif response.status_code == 404:
        assert response_json["message"] == "User not found"

    print(f"GET request executed for username '{username}'")
    