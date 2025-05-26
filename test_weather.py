from playwright.sync_api import sync_playwright

def test_weather_api():
    with sync_playwright() as p:
        # create an API context
        request_context = p.request.new_context()

        #Base URL for the weather API
        base_url = "https://api.open-meteo.com/v1/forecast"

        # Test a valid request
        params = {
            "latitude": 41.0812,
            "longitude": 81.5188,
            "past_days": 3
        }
        response = request_context.get(base_url, params=params)
        assert response.status == 200, f"Expected 200, got {response.status}"

        # Parse the JSON response
        data = response.json()
        print("Response data: %s", data)

        # Check if the response contains the expected keys
        assert "timezone" in data, "Response should contain 'timezone' key"
        print("Request successful: %s", data)

test_weather_api()