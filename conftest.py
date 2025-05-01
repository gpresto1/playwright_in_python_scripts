import pytest
from playwright.sync_api import sync_playwright, APIRequestContext

@pytest.fixture(scope="session")
def playwright_instance():
    """Set up a Playwright instance for the test session."""
    with sync_playwright() as playwright:
        yield playwright

@pytest.fixture(scope="session")
def api_request_context(playwright_instance) -> APIRequestContext:
    """Set up an APIRequestContext for the test session."""
    request_context = playwright_instance.request.new_context(
        base_url="https://pokeapi.co/api/v2/"  # Base URL for PokeAPI
    )
    yield request_context
    request_context.dispose()

@pytest.fixture(scope="function")
def page(playwright_instance):
    """Set up a new browser page for each test."""
    browser = playwright_instance.chromium.launch(headless=False)  # Set headless=True to run in headless mode
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
    browser.close()

