'''
ĆWICZENIE 4

Napisz funkcję o nazwie stworz_album(), która buduje słownik opisujący album muzyczny.
Funkcja powinna przyjmować nazwę artysty i tytuł albumu, a następnie zwracać słownik
zawierający te dwie informacje.

Użyj funkcji, aby utworzyć trzy słowniki reprezentujące różne albumy.
Wydrukuj każdą wartość zwracaną, aby pokazać, że słowniki poprawnie przechowują
informacje o albumie.

Użyj, None aby dodać opcjonalny parametr, stworz_album()który pozwala Ci przechowywać
liczbę utworów w albumie. Jeśli linia wywoławcza zawiera wartość liczby utworów,
dodaj tę wartość do słownika albumu. Wykonaj co najmniej jedno nowe wywołanie funkcji,
które zawiera liczbę utworów w albumie.
'''


def stworz_album(artysta, tytul, liczba_utworow = "None"):

    if liczba_utworow == 0:
        liczba_utworow = "None"
    
    album = {"artysta": artysta, "tytul": tytul, "liczba_utworow": liczba_utworow}
    return album


Renaissance = stworz_album("Beyonce", "Renaissance")
album2 = stworz_album("Taylor Swift", "Midnights")
album3 = stworz_album("Adele", "30", 12)


print(Renaissance)
print(album2)
print(album3)