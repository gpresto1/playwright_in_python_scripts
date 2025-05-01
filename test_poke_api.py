import re
import json
from playwright.sync_api import APIRequestContext, expect

def test_get_pokemon(api_request_context: APIRequestContext):
    response = api_request_context.get("pokemon/pikachu")  # Example: Get Pikachu data

    # Assert the response status
    assert response.status == 200
    assert response.ok

    # Assert the response JSON data
    data = response.json()
    assert data["name"] == "pikachu"

    # Assert the "content-type" header
    assert "content-type" in response.headers
    assert response.headers["content-type"] == "application/json; charset=utf-8"
