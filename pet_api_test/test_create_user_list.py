from playwright.sync_api import sync_playwright
import time


def test_create_user_with_list():

    payload = [
        {
            "id": 101,
            "username": "markuser",
            "firstName": "Mark",
            "lastName": "Labiseg",
            "email": "mark@example.com",
            "password": "password123",
            "phone": "09123456789",
            "userStatus": 1
        }
    ]

    with sync_playwright() as p:

        api_context = p.request.new_context()

        start_time = time.time()

        response = api_context.post(
            "https://petstore.swagger.io/v2/user/createWithList",
            data=payload
        )

        response_time = time.time() - start_time

        # Status Code Validation
        assert response.status == 200, (
            f"Expected status code 200 but got {response.status}"
        )

        # Header Validation
        headers = response.headers
        assert "application/json" in headers.get(
            "content-type", ""
        ), "Content-Type is not application/json"

        # Response Body Validation
        body = response.json()

        assert body is not None, "Response body is empty"

        assert "code" in body, "Field 'code' is missing"
        assert "type" in body, "Field 'type' is missing"
        assert "message" in body, "Field 'message' is missing"

        # Field Value Validation
        assert body["code"] == 200, (
            f"Expected code=200 but got {body['code']}"
        )

        assert body["message"] == "ok", (
            f"Expected message='ok' but got {body['message']}"
        )

        assert isinstance(body["code"], int), (
            "code should be integer"
        )

        assert isinstance(body["message"], str), (
            "message should be string"
        )

        # Response Time Validation
        assert response_time < 5, (
            f"Response time exceeded threshold: {response_time:.2f}s"
        )

        print("===================================")
        print("API Test Passed")
        print(f"Status Code : {response.status}")
        print(f"Response    : {body}")
        print(f"Response Time: {response_time:.2f}s")
        print("===================================")