from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    request_context = p.request.new_context()
    response = request_context.get("https://jsonplaceholder.typicode.com/users/1")

    status = response.status
    print(f"Status odpowiedzi: {status}")
    assert status == 200

    #pobranie odpowiedzi z zapytania GET jako json
    result = response.json()
    name = result["name"]
    print(f"Uzytkownik nazywa się {name}.")



# połączeie  do Google
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.google.pl/?hl=pl")
    page.click("#L2AGLb")
    page.fill("#APjFqb", name)
    page.click("input[value='Szukaj w Google']")  #page.press("textarea", 'Enter')
    print(f"Wyniki wyszukiwania dla {name}")

    page.wait_for_timeout(10000)

    browser.close()