# CWICZENIE 3
# Napisz funkcję miasta_panstwa(), która akceptuje nazwę miasta i jego kraju.
# Dodaj tez argument ludnosc, który powinien być liczbą całkowitą. Jesli ludnosc rowna sie 0, to niech zwroci NaN
# Funkcja powinna wydrukować proste zdanie, takie jak "Warszawa jest w kraju Polska".
# Podaj parametrowi kraju wartość domyślną.
# Wywołaj swoją funkcję dla trzech różnych miast, z których przynajmniej jedno nie znajduje się w domyślnym kraju.

def  miasta_panstwa(miasto, ludnosc, kraj = "Polska"):  #nie moze byc miasto, kraj = Poslka, ludnosc, bo wtedy nie bedzie domyslnej wartosci dla kraju
    
    if ludnosc == 0:
        ludnosc = "NaN"

    miasta_panstwa_slownik = {"kraj": kraj, "miasto": miasto, "ludnosc": ludnosc}
    return miasta_panstwa_slownik

Warszawa = miasta_panstwa("Warszawa", 1790658)
miasto2 = miasta_panstwa("Kraków", 779115)
miasto3 = miasta_panstwa("Berlin", 0, "Niemcy")


print(f"{Warszawa['miasto']} jest w kraju {Warszawa['kraj']} z ludnością {Warszawa['ludnosc']}")
print(f"{miasto2['miasto']} jest w kraju {miasto2['kraj']} z ludnością {miasto2['ludnosc']}")
print(f"{miasto3['miasto']} jest w kraju {miasto3['kraj']} z ludnoscia {miasto3['ludnosc']}")
