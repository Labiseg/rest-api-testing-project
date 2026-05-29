import requests

BASE_URL = "https://petstore.swagger.io/v2/store/inventory"


def test_get_store_inventory():
    response = requests.get(BASE_URL)

    assert response.status_code == 200, (
        f"Expected 200 but got {response.status_code}"
    )

    inventory = response.json()

    assert isinstance(inventory, dict)