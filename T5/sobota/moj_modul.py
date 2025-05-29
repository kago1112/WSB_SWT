# tworzymy prosty moduł i wykorzystujemy go w innym pliku


# przywitaj sie
def przywitaj(imie):
    #Funkcja witajaca z podanym imieniem
    print(f"Czesc {imie}! Milo Cie poznac.")



# przywitaj sie wraz z nazwa uzytkownika
import getpass

username = getpass.getuser()

def przywitaj_sie(imie):
    #Funkcja witajaca z podanym imieniem
    print(f"Czesc {imie}! Jestem {username}. Milo Cie poznac.")





# policz do 3
def policz_do_trzech():
    #Funkcja wpisujaca kolejne liczby od 1 do 3
    for i in range(1,4):
        print(i)

wiadomosc_powitalna = "Witaj w moim module!"




