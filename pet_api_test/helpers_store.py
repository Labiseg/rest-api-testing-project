import requests

from pet_api_test.test_data import STORE_INVENTORY_URL

BASE_URL = "https://petstore.swagger.io/v2/store/inventory"


# ---------------- Helper Function ----------------
def get_store_inventory():

    response = requests.get(
        BASE_URL,
        headers={
            "accept": "application/json"
        }
    )

    return response

import requests

BASE_URL = "https://petstore.swagger.io/v2/user"


# ---------------- Helper Function ----------------
def update_store_user(username, user_data):

    response = requests.put(
        f"{BASE_URL}/{username}",
        json=user_data,
        headers={
            "Content-Type": "application/json",
            "accept": "application/json"
        }
    )

    return response

import requests

BASE_URL = "https://petstore.swagger.io/v2/user"


# ---------------- Helper Function ----------------
def delete_store_user(username):

    response = requests.delete(
        f"{BASE_URL}/{username}",
        headers={
            "accept": "application/json"
        }
    )

    return response