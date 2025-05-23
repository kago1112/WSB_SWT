# CWICZENIE 3
# Napisz funkcję miasta_panstwa(), która akceptuje nazwę miasta i jego kraju.
# Funkcja powinna wydrukować proste zdanie, takie jak "Warszawa jest kraju Polska".
# Podaj parametrowi kraju wartość domyślną.
# Wywołaj swoją funkcję dla trzech różnych miast, z których przynajmniej jedno nie znajduje się w domyślnym kraju.


def miasta_panstwa(miasto, ludnosc  = 0, kraj = "Polska"):

    # sprawdzenie czy ludnosc jest rowna 0
    if ludnosc == 0:
        ludnosc = "NaN"

    miasto_panstwo_slownik = {"kraj": kraj, "miasto": miasto, "ludnosc": ludnosc}
    return miasto_panstwo_slownik

miasto_funkcja = miasta_panstwa("Warszawa")
print(miasto_funkcja)