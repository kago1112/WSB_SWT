from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    # przechodzimy do strony logowania
    page.goto("https://practicetestautomation.com/practice-test-login/")
    # wprowadzenie username, zbadaj i skopiuj Xpath (selenium) albo id w kodzie źrodłowym, wraz z " oraz #
    # # wskazuje na id
    # page.fill(//*[@id="username"]), oraz dodajemy targetową wartość tego elementu
    page.fill("#username", "student")
    # to samo robimy z hasłem
    page.fill("#password", "Password123") 
    # niebezpiecznie jest podawanie danych jak haslo w kodzie - lepiej jest zapisac haslo jako zmienna srodowiskowa
    #klikniecie przycisku submit
    page.click("#submit")

    # czekamy, az nasza strona bedzie miala url successful logowania
    page.wait_for_url("**/logged-in-successfully/")
    # ** oznacza, ze moze byc jakikolwiek prefix przed tym url

    # logged in successfully 1
    assert page.url in "https://practicetestautomation.com/logged-in-successfully/"
    if page.url == "https://practicetestautomation.com/logged-in-successfully/":
        print("Zalogowano pomyślnie, strona ma poprawny URL.")

    # logged in successfully 2
    success_message = "Logged In Successfully"
    message = page.text_content("h1")  # pobieramy zawartość nagłówka h1, w ktorym znajduje się komunikat o pomyślnym zalogowaniu
    print(f"Zawartosc naglowka to {message}")

    assert success_message in message
    
    # sprawdzemnie, czy element z tekstem log out jest widoczny na stronie
    # dzięki locator możemy zlokalizować element na stronie
    # is_visible() sprawdza, czy element jest widoczny na stronie
    locator_logout = page.locator("text=Log out").is_visible()
    assert locator_logout is True

    browser.close()