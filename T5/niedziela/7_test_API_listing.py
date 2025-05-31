from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    request_context = p.request.new_context()
    response = request_context.get("https://jsonplaceholder.typicode.com/posts")
    status = response.status

    print(f"Status odpowiedzi: {status}")
    assert status == 200

    posts = response.json()   # pobieramy odpowiedź w formacie JSON
    assert isinstance(posts, list)   # sprawdzamy, czy odpowiedź jest listą
    
    if len(posts) > 0:
        print(f"W aplikacji znajduje sie {len(posts)} postów.")

        print(f"Sprawdzenie czy w aplikacji znajduje sie 100 postow...")
        assert len(posts) == 100
        if len(posts) == 100:
            print("W aplikacji znajduje sie 100 postów.")