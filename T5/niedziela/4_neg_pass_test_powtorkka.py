from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://practicetestautomation.com/practice-test-login/")
    page.fill("#username", "student")
    page.fill("#password", "incorrectPassword")
    page.click("#submit")

    # 1 test - url
    current_url = page.url
    print(f"Aktualny URL to {current_url}")
    assert "/practice-test-login/" in current_url

    # 2 test - error message
    error_text = page.text_content("Your password is invalid!")
    print(f"Komuniat błędu to: {error_text}")
    assert error_text == "Your password is invalid!"

    browser.close()
