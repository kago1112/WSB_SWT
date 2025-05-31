from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    #utworzyc kontest API - inny niz przegladarki
    request_context = p.request.new_context()

    #przygotowanie danych do wyslania; deklaracja danych nowego posta
    new_post = {"userId": 9, "title": "title sample", "body": "body sample"}
    print(f"Wysyłamy nowy post: {new_post}")

    #wysyłamy zadanie POST do API aby utworzyc nowy post
    #data= new_post - dane do wysłania w formacie JSON
    #request_context.post - wysyła żądanie POST do podanego URL
    response = request_context.post("https://jsonplaceholder.typicode.com/posts",data=new_post)

    status = response.status
    print("Status: ",status)
    assert status == 201

    result = response.json()
    print(f"Zawartość nowego posta to: {result}")

    #sposob 1
    assert result["userId"] == 9
    assert result["title"] == "title sample"
    assert result["body"]  == "body sample"

    #sposob 2
    assert result["userId"] == new_post["userId"]
    assert result["title"] == new_post["title"]
    assert result["body"] == new_post["body"]