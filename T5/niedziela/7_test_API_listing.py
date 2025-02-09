from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    request_context = p.request.new_context()
    response = request_context.get("https://jsonplaceholder.typicode.com/posts")
    status = response.status

    print(f"Status odpowiedzi: {status}")
    assert status == 200

    result = response.json()
    assert isinstance(result, list)
    
    if len(result) > 0:
        print(f"W aplikacji znajduje sie {len(result)} postów.")

        print(f"Sprawdzenie czy w aplikacji znajduje sie 100 postow...")
        assert len(result) == 100
