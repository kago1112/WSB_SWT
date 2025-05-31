from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    #utwórz kontekst API - inny niz przeglądarki
    request_context = p.request.new_context()
    #wysyłamy ządanie GET do API
    response = request_context.get("https://jsonplaceholder.typicode.com/posts/1")
    #sprawdzamy status odpowiedzi
    status = response.status

    print(f"Status odpowiedzi to: {status}")
    assert status == 200

    body = response.json()
    print(body)

    id = body["id"] #spodziewamy się 1
    userid = body["userId"] #spodziewamy się 1
    title = body["title"]
    body = body["body"]

    print(f"Id to {id}.")
    print(f"UserId to {userid}.")
    print(f"Title to {title}.")
    print(f"Body to {body}.")

    assert id == 1
    assert userid == 1
    assert title == "sunt aut facere repellat provident occaecati excepturi optio reprehenderit"
    assert body == "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"

    # sprawdzamy, czy tytuł jest stringiem
    print("Typ title to string: ", isinstance(title,str))
    assert isinstance(title, str)

    # sprawdzamy, czy id jest intergerem
    print(f"Typ id to integer: ", isinstance(id, int))
    assert isinstance(id, int)