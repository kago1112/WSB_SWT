import random

#losujemy liczbe z przedzialu 1-10

losowa = random.randint(1,10)
print(f"Wynik losowania z liczb z zakresu 1 do 10 to: {losowa}")


#wylosujmy 5 liczb  z zakresu  od 1 do 10 i zapisujemy je do listy

lista_losowych = random.sample(range(1,11),5)
print(f"Lista liczb wylosowanych z zakresu 1 do 10 to: {lista_losowych}")
