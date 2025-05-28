# CWICZENIE 3
# Napisz funkcję miasta_panstwa(), która akceptuje nazwę miasta i jego kraju.
# Dodaj tez argument ludnosc, który powinien być liczbą całkowitą.
# Funkcja powinna wydrukować proste zdanie, takie jak "Warszawa jest w kraju Polska".
# Podaj parametrowi kraju wartość domyślną.
# Wywołaj swoją funkcję dla trzech różnych miast, z których przynajmniej jedno nie znajduje się w domyślnym kraju.


def miasta_panstwa(miasto, ludnosc, kraj = "Polska"):

    # sprawdzenie czy ludnosc jest rowna 0
    if ludnosc == 0:
        ludnosc = "NaN"

    miasto_panstwo_slownik = {"kraj": kraj, "miasto": miasto, "ludnosc": ludnosc}
    return miasto_panstwo_slownik


# Wywołanie funkcji dla trzech różnych miast
miasto1 = miasta_panstwa("Warszawa", 1790658)
miasto2 = miasta_panstwa("Kraków", 779115)
miasto3 = miasta_panstwa("Berlin", 0, "Niemcy")

# Wyświetlenie wyników
print(f"{miasto1["miasto"]} jest w kraju {miasto1["kraj"]} z ludnością {miasto1["ludnosc"]}")
print(f"{miasto2["miasto"]} jest w kraju {miasto2["kraj"]} z ludnością {miasto2["ludnosc"]}")
print(f"{miasto3["miasto"]} jest w kraju {miasto3["kraj"]} z ludnością {miasto3["ludnosc"]}")