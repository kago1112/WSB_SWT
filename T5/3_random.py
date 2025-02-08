import random

#losujemy liczbe z przedzialu 1-10 (sposob 1)
losowa = random.randint(1,10)
print(f"Wynik losowania z liczb z zakresu 1 do 10 to: {losowa}")


#losujemy liczbe z przedzialu 1-10 (sposob 2, z inputem i int)
liczba_1 = int(input("Podaj liczbe 1: "))
liczba_2 = int(input("Podaj liczbe 2: "))
losowa = random.randint(liczba_1,liczba_2)
print(f"Wynik losowania z liczb z zakresu {liczba_1} do {liczba_2} to: {losowa}")


#losujemy 5 liczb  z zakresu  od 1 do 10 i zapisujemy je do listy
lista_losowych = random.sample(range(1,11),5)
print(f"Lista liczb wylosowanych z zakresu 1 do 10 to: {lista_losowych}")
