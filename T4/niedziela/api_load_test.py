import time
import requests


url = "https://jsonplaceholder.typicode.com/posts"  # URL for the API endpoint

def send_request():     # Ta funkcja wysyła pojedyncze zapytanie GET do API i zwraca kod statusu (np. 200, 400, 500, ...)
    response = requests.get(url)  # Wysyłamy zapytanie GET do API
    return response.status_code  # Zwracamy kod statusu odpowiedzi

print("Rozpoczy namy prosty test, będziemy wysyłać 10 zapytań do API")

start_time = time.time()  # Pobieramy aktualny czas przed rozpoczęciem testu

# w petli bedziemy wyslac 10 zapytn od zakresu 1-10
for  i in range(10):  # Wysyłamy 10 zapytań do API
    status = send_request()  # Wywołujemy funkcję wysyłającą zapytanie
    print(f"Zapytanie numer {i + 1} zwróciło status: {status}")  # Wyświetlamy status odpowiedzi

end_time = time.time()  # Pobieramy czas po zakończeniu testu
elapsed_time = end_time - start_time  # Obliczamy czas trwania testu

print(f"Suma czasu dla 10 zapytań to: {round(elapsed_time, 2)} sekund")  # Wyświetlamy czas wykonania testu
print("Test zakończony.")  # Informujemy o zakończeniu testu