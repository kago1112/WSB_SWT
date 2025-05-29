class Pies:
    # klasa reprezentująca psa

    def __init__(self, nazwa, wiek):
        # konstruktor
        self.nazwa = nazwa
        self.wiek = wiek
    
    def szczekaj(self):
        # metoda: pies szczeka
        print(f"{self.nazwa} szczeka: Hau Hau!")
    
    def przelicz_wiek(self):
        # metoda: zwraca ludzki wiek psa
        return self.wiek * 7
    


pies_1 = Pies("Reksio", 5)

pies_1.szczekaj()  # oczekujemy: Reksio szczeka: Hau Hau!
print(pies_1.wiek)

print(pies_1.przelicz_wiek())

print(pies_1.szczekaj())