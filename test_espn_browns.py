import re
from playwright.sync_api import Page, expect


def test_navigates_to_browns(page: Page):
    page.goto("https://www.espn.com/")
    expect(page.get_by_role("link", name="NFL", exact=True)).to_be_visible()
    page.get_by_role("link", name="NFL", exact=True).hover()
    page.pause()
   # expect(page.get_by_role("link", name="Teams")).to_be_visible()
   # page.get_by_role("link", name="Teams").click()
   # page.pause()
    expect(page.locator("a").filter(has_text="Cleveland Browns")).to_be_visible()
    page.locator("a").filter(has_text="Cleveland Browns").click()