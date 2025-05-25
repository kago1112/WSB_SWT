# liczba pierwsza - iczba naturalna większa od 1, która ma dokładnie dwa dzielniki naturalne: jedynkę i siebie samą

def czy_pierwsza(n):
    if n <= 1:              #1 nie jest liczba pierwsza, wiec musimy ja wyeliminowac
        return False
    for i in range(2, n):   
        if n % i == 0:     #jesli n dzieli sie przez i to nie jest liczba pierwsza
            return False
    return True             #jesli nie znalazlismy dzielnika to jest liczba pierwsza

print(czy_pierwsza(1))      #False
print(czy_pierwsza(2))      #True
print(czy_pierwsza(3))      #True
print(czy_pierwsza(6))       #False
print(czy_pierwsza(10))     #False