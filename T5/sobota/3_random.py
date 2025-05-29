'''
Napisz program który wylosuje 5 liczb całkowitych z zakresu 1 - 100 i wyświetli je na ekranie. 
 
Założenia:
Wykorzystaj do tego moduł random. 
Liczby mogą się powtarzać. 
Wykorzystaj do tego pętle. 
Wynik ma być zapisany w liście

Wynik:
Jako wynik chciałbym otrzymać output na konsoli jako:
Wylosowane liczby to: ....
'''

# random.randit - losuje liczbę z przedziału (a,b) włącznie
# input - pobiera dane od użytkownika
# int - konwertuje dane do typu całkowitego
# sample - losuje unikalne liczby z podanego zakresu, bez powtórzeń
# range - tworzy zakres liczb, np. range(1,101) tworzy liczby od 1 do 100


import random



#losujemy liczbe z przedzialu 1-100 (sposob 1)
losowa = random.randint(1,100)
print(f"Wynik losowania z liczb z zakresu 1 do 100 to: {losowa}")




#losujemy liczbe z przedzialu 1-10 (sposob 2, z inputem i int)
liczba_1 = int(input("Podaj liczbe 1: "))
liczba_2 = int(input("Podaj liczbe 2: "))
losowa = random.randint(liczba_1,liczba_2)
print(f"Wynik losowania z liczb z zakresu {liczba_1} do {liczba_2} to: {losowa}")



#losujemy 5 liczb  z zakresu  od 1 do 100 i zapisujemy je do listy
lista_losowych = random.sample(range(1,101),5)
print(f"Lista pięciu liczb wylosowanych z zakresu 1 do 100 to: {lista_losowych}")