'''
Utwórz moduł o naziwe figury.py a w nim zdefiniuj dwie klasy - Kwadrat i Kolo.
 
Klasa Kwadrat:
pownna mieć atrybut dlugosc_boku w konstruktorze init. 
powinna miec metodę powierzchnia(self) która oblicza pole kwadratu i zwraca wynik (return)
Klasa Kolo:
powinna mieć atrybut promien ustawiany w konstruktorze (init)
powinna mieć metodę powierzchnia(self) i zwracająca wynik (return)
Następnie w głównym skrypcie (plik o nazwie test_figury.py), importujecie klasy Kwadrat i Kolo z modułu figury. 
 
Utwórz instancję/obiekt kwadrat o wybranej długości kołu, tak samo dla obiektu koło.
 
Wyświetl następnie wartości na konsolę (print):
Pole kwadratu o boku 3 = 15.00
Pole koła o promieniu 3 = XX
'''



import math


class Kwadrat:
    def __init__(self, dlugosc_boku):
        self.dlugosc_boku = dlugosc_boku
    
    def powierzchnia(self):
        return self.dlugosc_boku ** 2
    
    def obwod(self):
        return 4 * self.dlugosc_boku



class Kolo:
    def __init__(self, promien):
        self.promien = promien
    
    def powierzchnia(self):
        return math.pi * (self.promien ** 2)
