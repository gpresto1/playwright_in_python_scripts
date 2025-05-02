import re
from playwright.sync_api import Page, expect


def test_navigates_to_myles_bio(page: Page):
    # Flows from homepage to Myles Garrett bio
    page.goto("https://www.espn.com/")
    
    # Confirms that the NFL tab is visible
    expect(page.get_by_role("link", name="NFL", exact=True)).to_be_visible()
    page.get_by_role("link", name="NFL", exact=True).hover()
    
    # Confirms that the Teams tab is visible and clicks it
    expect(page.get_by_role("link", name="Teams", exact=True)).to_be_visible()
    page.get_by_role("link", name="Teams", exact=True).click()
    
    # Confirms Cleveland Browns link is visible and clicks it
    expect(page.locator("a").filter(has_text="Cleveland Browns")).to_be_visible()
    page.locator("a").filter(has_text="Cleveland Browns").click()
    
    # Confirms Roster link is visible and clicks it
    expect(page.get_by_role("link", name="Roster")).to_be_visible()
    page.get_by_role("link", name="Roster").click()
    
    # Confirms Myles Garrett link is visible and clicks it
    expect(page.get_by_role("link", name="Myles Garrett")).to_be_visible()
    page.get_by_role("link", name="Myles Garrett").click()
    
    # Confirms Bio link is visible and clicks it
    expect(page.get_by_role("link", name="Bio")).to_be_visible()
    page.get_by_role("link", name="Bio").click()


def test_navigates_to_cleveland_cavs(page: Page):
    # Flows from homepage to Cavs homepage
    page.goto("https://www.espn.com/")
    
    # Confirms that the NBA tab is visible and hovers
    expect(page.get_by_role("link", name="NBA", exact=True)).to_be_visible()
    page.get_by_role("link", name="NBA", exact=True).hover()
    
    # Confirms that the Teams tab is visible and clicks it
    expect(page.get_by_role("link", name="Teams", exact=True)).to_be_visible()
    page.get_by_role("link", name="Teams", exact=True).click()
    
    # Confirms Cleveland Cavaliers link is visible and clicks it
    expect(page.locator("a").filter(has_text="Cleveland Cavaliers")).to_be_visible()
    page.locator("a").filter(has_text="Cleveland Cavaliers").click()
    
     # Confirms that the Cleveland Cavaliers page has loaded by checking for the "Cleveland" and "Cavaliers" spans
    expect(page.locator("span.db.pr3.nowrap").filter(has_text="Cleveland")).to_be_visible()
    expect(page.locator("span.db.fw-bold").filter(has_text="Cavaliers")).to_be_visible()