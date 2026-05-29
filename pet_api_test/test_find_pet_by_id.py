import requests
import pytest

BASE_URL = "https://petstore.swagger.io/v2/pet"

# ---------------- Test Data ----------------

valid_pet = {
    "id": 1010,
    "category": {
        "id": 1,
        "name": "Dogs"
    },
    "name": "doggie",
    "photoUrls": ["string"],
    "tags": [
        {
            "id": 1,
            "name": "tag1"
        }
    ],
    "status": "available"
}

invalid_pet_id = 2002
