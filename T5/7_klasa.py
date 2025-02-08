class Samochod:
    # definicja klasy
    def __init__(self, marka, model): 
        # self - odwolanie do aktualnego obiektu, reprezentuje nowostworzona instancje/obiekt
        self.marka = marka # ustawiamy atrybut 'marka obiektu'
        self.model = model
        self.predkosc = 0 # ustawiamy predkosc poczatkowa samochodu jako 0 km/h
        self.wlaczony_silnik = False
    
    def uruchom_silnik(self):
        print("Silnik został uruchomiony")
        self.wlaczony_silnik = True
    
    def przyspiesz(self, wartosc):
        # zakladamy, ze atrybut predkosc istnieje
        self.predkosc += wartosc

moj_samochod = Samochod("Toyota", "Yaris")
# albo (????)
# moj_samochod_2 = Samochod.__init__(self, "Toyota", "Yaris")

#moj_samochod.uruchom_silnik()
#moj_samochod.przyspiesz(50)

#print(moj_samochod.wlaczony_silnik)
#print(moj_samochod.predkosc)




moj_samochod_2 = Samochod("BMW", "5")

print(moj_samochod_2.predkosc)
print(moj_samochod_2.wlaczony_silnik)

moj_samochod_2.uruchom_silnik()
print(moj_samochod_2.wlaczony_silnik)

moj_samochod_2.przyspiesz(100)
print(moj_samochod_2.predkosc)