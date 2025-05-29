class Samochod:
    # definicja klasy
    def __init__(self, marka, model): 
        # self - odwolanie do aktualnego obiektu, reprezentuje nowostworzona instancje/obiekt
        self.marka = marka # ustawiamy atrybut 'marka obiektu'
        self.model = model
        self.predkosc = 0 # ustawiamy predkosc poczatkowa samochodu jako 0 km/h
        self.wlaczony_silnik = False
        self.kolor = "czerwony"  # domyślny kolor samochodu
    
    def uruchom_silnik(self):
        print("Silnik został uruchomiony")
        self.wlaczony_silnik = True     # ustawiamy atrybut wlaczony_silnik na True, czyli silnik jest wlaczony
    
    def przyspiesz(self, wartosc):
        # zakladamy, ze atrybut predkosc istnieje
        self.predkosc += wartosc
        # += oznacza, ze do aktualnej wartosci predkosci dodajemy wartosc podana w argumencie funkcji
    
    def zwolnij(self, wartosc):
        self.predkosc -= wartosc
        if self.predkosc < 0:
            self.predkosc = 0



moj_samochod = Samochod("Toyota", "Yaris")

#moj_samochod.uruchom_silnik()
#moj_samochod.przyspiesz(50)

#print(moj_samochod.wlaczony_silnik)
#print(moj_samochod.predkosc)




moj_samochod_2 = Samochod("BMW", "5")

print(f"Startowa predkosc samochodu wynosi {moj_samochod_2.predkosc} km/h")
print(f"Czy samochod jest uruchomiony?: {moj_samochod_2.wlaczony_silnik}")

moj_samochod_2.uruchom_silnik()
print(f"Czy samochód jest uruchomiony?: {moj_samochod_2.wlaczony_silnik}")
print("Przyspieszam")
moj_samochod_2.przyspiesz(100)

print(f"Obecna prędkość samochodu {moj_samochod_2.marka} {moj_samochod_2.model} wynosi {moj_samochod_2.predkosc} km/h")

moj_samochod_2.przyspiesz(50)
print("Przyspieszam")
print(f"Obecna prędkość samochodu {moj_samochod_2.marka} {moj_samochod_2.model} wynosi {moj_samochod_2.predkosc} km/h")

moj_samochod_2.zwolnij(30)
print("Zwalniam")
print(f"Obecna prędkość samochodu {moj_samochod_2.marka} {moj_samochod_2.model} wynosi {moj_samochod_2.predkosc} km/h")

moj_samochod_2.zwolnij(150)
print("Zwalniam")
print(f"Obecna prędkość samochodu {moj_samochod_2.marka} {moj_samochod_2.model} wynosi {moj_samochod_2.predkosc} km/h")