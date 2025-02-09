from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False) # startujemy przeglądarkę, headless=False włącza nam tę stronę w przeglądarce
    page = browser.new_page() # otwieramy nową kartę
    page.goto("https://onet.pl") # przechodzimy na stronę
    page_title = page.title() # pobieramy tytuł strony
    print(f"Tytuł strony to {page_title}") # drukujemy na konsole tytul strony

    assert "Onet – Jesteś na bieżąco" in page_title # sprawdzamy, czy tytul strony zawiera oczekiwany tekst

    browser.close() # zamykamy przegladarke