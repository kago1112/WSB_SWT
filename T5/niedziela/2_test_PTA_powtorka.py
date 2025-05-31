from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://practicetestautomation.com/practice-test-login/")
    page.fill("#username",  "student")   
        # wprowadzenie username, zbadaj i skopiuj Xpath (selenium) albo id w kodzie źrodłowym, wraz z " oraz # (# pokazuje,ze element jest identyfikatorem, czyli id, a nie klasą)
    page.fill("#password", "Password123")
    page.click("#submit")


    page.wait_for_url("**/logged-in-successfully/")  # czekamy, az nasza strona bedzie miala url successful logowania

    # trudniej - sprawdzamy, czy strona ma poprawny URL po zalogowaniu
    assert page.url in "https://practicetestautomation.com/logged-in-successfully/"
    success_message = "Logged In Successfully"
    message = page.text_content("h1")  # pobieramy zawartość nagłówka h1, w ktorym znajduje się komunikat o pomyślnym zalogowaniu
    print(f"Zawartosc naglowka to {message}")
    assert message in success_message

    # prosciej - sprawdzamy, czy strona ma poprawny URL po zalogowaniu
    assert page.url == "https://practicetestautomation.com/logged-in-successfully/"  # sprawdzamy, czy url jest taki, jak oczekiwany
    if page.url == "https://practicetestautomation.com/logged-in-successfully/":
        print("Zalogowano pomyślnie, strona ma poprawny URL.")

    locator_logout = page.locator("text=Log out").is_visible()  # sprawdzenie, czy element z tekstem log out jest widoczny na stronie
    assert locator_logout is True
    if locator_logout is True:
        print("Element 'Log out' jest widoczny na stronie.")

    browser.close()  # zamykamy przegladarke