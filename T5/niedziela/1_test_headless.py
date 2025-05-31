from playwright.sync_api import sync_playwright


#domyślnie playwright jest w formie headless

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://onet.pl")
    page_title = page.title()   # pobieramy tytuł strony
    print(f"Tytuł strony to {page_title}") # drukujemy na konsole tytul strony

    assert "Onet – Jesteś na bieżąco" in page_title # sprawdzamy, czy tytul strony zawiera oczekiwany tekst

    browser.close() # zamykamy przegladarke