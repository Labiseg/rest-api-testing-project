import requests

BASE_URL = "https://petstore3.swagger.io/api/v3"
pet_id = 123456


def test_1_create_pet():
    payload = {
        "id": pet_id,
        "name": "testdog",
        "status": "available"
    }

    response = requests.post(f"{BASE_URL}/pet", json=payload)

    print("CREATE:", response.status_code, response.json())

    assert response.status_code == 200


def test_2_get_pet():
    response = requests.get(f"{BASE_URL}/pet/{pet_id}")

    print("GET:", response.status_code, response.json())

    assert response.status_code == 200
    assert response.json()["id"] == pet_id


def test_3_update_pet():
    payload = {
        "id": pet_id,
        "name": "updateddog",
        "status": "sold"
    }

    response = requests.put(f"{BASE_URL}/pet", json=payload)

    print("UPDATE:", response.status_code, response.json())

    assert response.status_code == 200


def test_4_delete_pet():
    response = requests.delete(f"{BASE_URL}/pet/{pet_id}")

    print("DELETE:", response.status_code)

    assert response.status_code in [200, 204]


def test_5_verify_deleted_pet():
    response = requests.get(f"{BASE_URL}/pet/{pet_id}")

    print("VERIFY DELETE:", response.status_code)

    assert response.status_code == 404