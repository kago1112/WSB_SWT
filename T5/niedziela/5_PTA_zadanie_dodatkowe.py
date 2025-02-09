from playwright.sync_api import sync_playwright

# odczytanie zawartosci pliku password.txt i ustawienie jego zawartości jako zmienna password
with open("password.txt") as file:
    password = file.read()

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://practicetestautomation.com/practice-test-login/")
    page.fill("#username", "student")
    page.fill("#password", password)
    page.click("#submit")

    page.wait_for_url("**/logged-in-successfully/")

    # logged in successfully 1
    assert page.url in "https://practicetestautomation.com/logged-in-successfully/"

    # logged in successfully 2
    success_message = "Logged In Successfully"
    message = page.text_content("h1")
    print(f"Zawartosc naglowka to {message}")

    assert success_message in message
    
    #sprawdzemnie, czy element z tekstem log out jest widoczny na stronie
    locator_logout = page.locator("text=Log out").is_visible()
    assert locator_logout is True

    browser.close()