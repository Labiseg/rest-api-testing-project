import requests

BASE_URL = "https://petstore.swagger.io/v2/user/createWithList"

def test_create_user_with_list():
    users = [
        {
            "id": 1,
            "username": "user1",
            "firstName": "Test",
            "lastName": "User",
            "email": "user1@test.com",
            "password": "password123",
            "phone": "1234567890",
            "userStatus": 1
        }
    ]

    response = requests.post(BASE_URL, json=users)

    assert response.status_code == 200