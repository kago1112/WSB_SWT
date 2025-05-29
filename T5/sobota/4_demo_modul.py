# tworzymy prosty moduł i wykorzystujemy go w innym pliku



import moj_modul #import naszego modulu

#uzycie funkcji z modulu
moj_modul.przywitaj("Kasia") # oczekiwany rezultat: "Czesc Kasia! Milo Cie poznac."
moj_modul.przywitaj_sie("Kasia")    # oczekiwany rezultat: " Czesc Kasia! Jestem <nazwa_uzytkownika>. Milo Cie poznac."

print(moj_modul.wiadomosc_powitalna)



print("Funkcja policz do 3 zwraca liczby: ")
moj_modul.policz_do_trzech() #powinno nam wydrukować liczby 1,2,3 w trzech linijkach