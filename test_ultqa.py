import re
from playwright.sync_api import Page, expect

def test_navigates_to_homepage(page: Page):
    page.goto("https://ultimateqa.com/automation/")

    # Expect page to contain specific text
    expect(page).to_have_title(re.compile("Automation Practice"))

def test_navigates_to_buttons(page: Page):
    # Navigate to the homepage
    test_navigates_to_homepage(page)

    # Click the big buttons link
    page.get_by_text("Big page with many elements").click()

    # Expect page to display headers
    page.locator("#Section_of_Buttons")
    page.locator("#Section_of_Social_Media_Follows")
    page.locator("#Section_of_Random_Stuff")

def test_fill_out_forms(page: Page):
    # Navigate to the homepage
    test_navigates_to_homepage(page)

    # Click the big buttons link
    test_navigates_to_buttons(page)

    #fill out the first contact form
    page.locator("#et_pb_contact_name_0").fill("John Doe")
    page.locator("#et_pb_contact_email_0").fill("JohnDoe@gmail.com")
    page.locator("#et_pb_contact_message_0").fill("This is a test message")
    page.locator('input[data-first_digit="8"][data-second_digit="6"]').fill("14")
    


    



