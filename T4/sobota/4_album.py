"""
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
"""


#Aby zadeklarować opcjonalny parametr, po prostu ustawiamy dla niego wartość domyślną podczas jego tworzenia . 
    # Jeśli nie przekażemy wartości, zostanie użyta wartość domyślna, jeśli przekażemy wartość, będzie to wartość parametru. 
    # Możliwe jest posiadanie wielu opcjonalnych parametrów.

def stworz_album(artysta, tytul, liczba_utworow = "None"):    

    if liczba_utworow == 0:
        liczba_utworow = "None"
    
    album = {"artysta": artysta, "tytul": tytul, "liczba utworow": liczba_utworow}
    return album

album1_funkcja = stworz_album("AAA", "AAA")
album2_funkcja = stworz_album("BBB", "BBB", 0)
album3_funkcja = stworz_album("CCC", "CCC", 110)

print(album1_funkcja)
print(album2_funkcja)
print(album3_funkcja)