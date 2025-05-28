import requests


url = "https://jsonplaceholder.typicode.com/posts"     # adres URL strony, do której wysyłamy zapytanie GET

print("Wysylamy zapytanie GET do: ", url)   # wysyłamy zapytanie GET do strony

response = requests.get(url)    # wysyłamy zapytanie GET i zapisujemy odpowiedź w zmiennej response

print("Otrzymaliśmy odpowiedz o statusie: ", response.status_code)  # wyświetlamy status odpowiedzi

if response.status_code == 200:
    data = response.json()
    print("Zawartosc strony to:", data)
else:
    print("Nie udalo sie pobrac danych ze strony/API")