import requests

# ---------------- Base URL ----------------
BASE_URL = "https://petstore.swagger.io/v2/store/order"

# ---------------- Test Data ----------------
store_order_payload = {
    "id": 0,
    "petId": 0,
    "quantity": 0,
    "shipDate": "2026-05-28T02:59:51.147Z",
    "status": "placed",
    "complete": True
}

# ---------------- TEST CASE ----------------
def test_create_store_order():

    response = requests.post(
        BASE_URL,
        headers={
            "accept": "application/json",
            "Content-Type": "application/json"
        },
        json=store_order_payload
    )

    # Validate status code
    assert response.status_code == 200, \
        f"Expected 200 but got {response.status_code}"

    # Only parse JSON if response has content
    if response.text:

        try:
            response_json = response.json()

            # Validate response structure
            assert "id" in response_json
            assert "petId" in response_json
            assert "quantity" in response_json
            assert "shipDate" in response_json
            assert "status" in response_json
            assert "complete" in response_json

            # Validate response values
            assert response_json["petId"] == store_order_payload["petId"]
            assert response_json["quantity"] == store_order_payload["quantity"]
            assert response_json["status"] == store_order_payload["status"]
            assert response_json["complete"] == store_order_payload["complete"]

            # Validate data types
            assert isinstance(response_json["id"], int)
            assert isinstance(response_json["petId"], int)
            assert isinstance(response_json["quantity"], int)
            assert isinstance(response_json["shipDate"], str)
            assert isinstance(response_json["status"], str)
            assert isinstance(response_json["complete"], bool)

            print("Response JSON:", response_json)

        except Exception:
            print("Response is not JSON")
            assert False, "Response could not be parsed as JSON"

    print("Store order created successfully")