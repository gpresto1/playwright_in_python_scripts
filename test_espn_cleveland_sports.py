import re
from playwright.sync_api import Page, expect


def test_navigates_to_myles_bio(page: Page):
    # flows from homepage to Myles Garrett bio
    page.goto("https://www.espn.com/")
    # confirms that the NFL tab is populating
    expect(page.get_by_role("link", name="NFL", exact=True)).to_be_visible()
    page.get_by_role("link", name="NFL", exact=True).hover()
    # moves to teams tab and selects cleveland browns
    page.get_by_role("link", name="Teams", exact=True).click()
    page.locator("a").filter(has_text="Cleveland Browns").click()
    # navigates to roster and then myles garrett bio
    page.get_by_role("link", name="Roster").click()
    page.get_by_role("link", name="Myles Garrett").click()
    page.get_by_role("link", name="Bio").click()

def test_navigates_to_cleveland_cavs(page: Page):
    # flows from homepage to Cavs homepage
    page.goto("https://www.espn.com/")
    # Confirms NBA tab is populating
    expect(page.get_by_role("link", name="NBA", exact=True)).to_be_visible()
    page.get_by_role("link", name="NBA", exact=True).hover()
    # naviagates to cavs page
    page.get_by_role("link", name="Teams", exact=True).click()
    page.locator("a").filter(has_text="Cleveland Cavaliers").click()
