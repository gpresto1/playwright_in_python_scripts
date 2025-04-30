import re
from playwright.sync_api import Page, expect


def test_navigates_to_myles_bio(page: Page):
    page.goto("https://www.espn.com/")
    expect(page.get_by_role("link", name="NFL", exact=True)).to_be_visible()
    page.get_by_role("link", name="NFL", exact=True).hover()
    page.get_by_role("link", name="Teams", exact=True).click()
    page.locator("a").filter(has_text="Cleveland Browns").click()
    page.get_by_role("link", name="Roster").click()
    page.get_by_role("link", name="Myles Garrett").click()
    page.get_by_role("link", name="Bio").click()

def test_navigates_to_cleveland_cavs(page: Page):
    page.goto("https://www.espn.com/")
    expect(page.get_by_role("link", name="NBA", exact=True)).to_be_visible()
    page.get_by_role("link", name="NBA", exact=True).hover()
    page.get_by_role("link", name="Teams", exact=True).click()
    page.locator("a").filter(has_text="Cleveland Cavaliers").click()
