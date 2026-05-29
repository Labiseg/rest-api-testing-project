import requests

BASE_URL = "https://petstore.swagger.io/v2/pet"



# ---------------- Helper Function ----------------
def get_pet_by_status(status):

    response = requests.get(
        f"{BASE_URL}/findByStatus",
        params={"status": status},
        headers={"accept": "application/json"}
    )

    return response
# ---------------- Helper Function ----------------
def add_pet(pet_data):
    """
    Helper function to add a pet via POST /pet
    Validates test data before sending.
    """

    response = requests.post(
        BASE_URL,
        json=pet_data
    )

    return response.json()

# ---------------- Helper Functions ----------------
def validate_pet_data(pet):
    assert isinstance(pet, dict), "Pet data must be a dictionary"
    assert "id" in pet, "Pet must have an 'id'"
    assert "category" in pet and "id" in pet["category"] and "name" in pet["category"], "Category must have id and name"
    assert "photoUrls" in pet and isinstance(pet["photoUrls"], list), "photoUrls must be a list"
    assert "tags" in pet and isinstance(pet["tags"], list), "tags must be a list"
    if "name" in pet:
        assert isinstance(pet["name"], str), "'name' must be a string"
    if "status" in pet:
        assert isinstance(pet["status"], str), "'status' must be a string"

def add_pet(pet_data):
    validate_pet_data(pet_data)
    headers = {"Content-Type": "application/json", "accept": "application/json"}
    response = requests.post(BASE_URL, json=pet_data, headers=headers)
    return response

def get_pet(pet_id):
    response = requests.get(f"{BASE_URL}/{pet_id}")
    return response

def delete_pet(pet_id):
    response = requests.delete(f"{BASE_URL}/{pet_id}")
    return response

def get_pet_by_id(pet_id):

    response = requests.get(
        f"{BASE_URL}/{pet_id}",
        headers={"accept": "application/json"}
    )

    return response 

# ---------------- Helper Functions ----------------
def delete_pet(pet_id):

    response = requests.delete(
        f"{BASE_URL}/{pet_id}",
        headers={
            "accept": "application/json",
            "api_key": "special_key"
        }
    )

    return response

# ---------------- Helper Functions ----------------
def create_pet():

    payload = {
        "id": 2001,
        "category": {
            "id": 1,
            "name": "Dogs"
        },
        "name": "buddy",
        "photoUrls": ["string"],
        "tags": [
            {
                "id": 1,
                "name": "tag1"
            }
        ],
        "status": "available"
    }

    response = requests.post(
        BASE_URL,
        json=payload,
        headers={
            "Content-Type": "application/json",
            "accept": "application/json"
        }
    )

    return response

# ---------------- Helper Functions ----------------

def add_pet(pet_data):

    response = requests.post(
        BASE_URL,
        json=pet_data,
        headers={
            "Content-Type": "application/json",
            "accept": "application/json"
        }
    )

    return response


if __name__ == "__main__":

    response = delete_pet(1)

    print("Status Code:", response.status_code)

    print("Response:", response.text)