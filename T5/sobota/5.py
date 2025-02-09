# Napisz program który wylosuje 5 liczb całkowitych z zakresu 1 - 100 i wyświetli je na ekranie. 
# Wykorzystaj do tego moduł random. Liczby mogą powtarzać. 
# Wykorzystaj do tego pętle
# Wynik ma byc zapisany w liscie 

import random


#z rozbiciem
wynik = [] # deklaracja listy

for i in range(5): #petla 5x
    liczba = random.randint(1,100) # zapisanie wartosci losowej do zmiennej
    wynik.append(liczba) #dodanie wartosci do listy

print(f"Wylosowane liczby to: {wynik}")




#bez rozbicia
lista_losowych_5 = []

for i in range(5):
    lista_losowych_5.append(random.randint(1,100))

print(f"Wylosowane liczby to: {lista_losowych_5}")