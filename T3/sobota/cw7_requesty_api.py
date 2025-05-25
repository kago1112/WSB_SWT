'''

Napisz prosty skrypt w Pythonie, który:
• Wysyła żądanie HTTP do wybranej strony internetowej, np. https://httpbin.org/status/200
• Sprawdza, czy strona jest dostępna, analizując kod statusu odpowiedzi (status 200 oznacza sukces).
• Wyświetla odpowiedni komunikat w konsoli:
    • "Test Passed: Strona jest dostępna", jeśli kod statusu to 200.
    • "Test Failed: Kod statusu: X", jeśli status jest inny niż 200, gdzie X to faktyczny kod statusu.

'''


# pip3 install requests
import requests

response = requests.get("https://jsonplaceholder.typicode.com/users")
print(response)
print(response.status_code)

if response.status_code == 200:
    print("Jupi! Strona jest OK")
#    print("Dane uzytkownikow to: ", response.json())
else:
    print(f"Ups, cos poszło nie tak, kod błedu to: {response.status_code}")
