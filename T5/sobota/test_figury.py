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



from figury import Kwadrat, Kolo
# import figury


bok = 5
kwadrat_1 = Kwadrat(bok)
pole_kwadratu = kwadrat_1.powierzchnia()
print(f"Pole kwadratu o boku {bok} wynosi {pole_kwadratu:.2f}")


promien = 3
kolo_1 = Kolo(promien)
pole_kola = kolo_1.powierzchnia()
print(f"Pole koła o promienu {promien} wynosi {pole_kola:.2f}")