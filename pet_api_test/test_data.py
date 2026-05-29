# ---------------- Store Inventory Test Data ----------------

STORE_INVENTORY_URL = "https://petstore.swagger.io/v2/store/inventory"

EXPECTED_STATUS_CODE = 200

EXPECTED_INVENTORY_STATUSES = [
    "available",
    "pending",
    "sold"
]
# ---------------- Store Order Test Data ----------------
# ---------------- Test Data ----------------
store_order_payload = {
    "id": 0,
    "petId": 0,
    "quantity": 0,
    "shipDate": "2026-05-28T02:59:51.147Z",
    "status": "placed",
    "complete": True
}

# ---------------- PET DATA ----------------

valid_pet = {
    "id": 1001,
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

invalid_pet_missing_name = {
    "id": 1002,
    "category": {
        "id": 1,
        "name": "Dogs"
    },
    "photoUrls": ["string"],
    "tags": [
        {
            "id": 1,
            "name": "tag1"
        }
    ],
    "status": "available"
}

invalid_pet_invalid_status = {
    "id": 1003,
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
    "status": "invalid_status"
}


# ---------------- PET IDS ----------------

valid_pet_id = 1
invalid_pet_id = 2002

# ---------------- Test Data ----------------
username = "Oreo"

updated_user = {
    "id": 1001,
    "username": "Oreo",
    "firstName": "Mark",
    "lastName": "Labiseg",
    "email": "oreo@example.com",
    "password": "password123",
    "phone": "09123456789",
    "userStatus": 1
}

