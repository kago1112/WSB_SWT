import math

# pow(co, do której potęgi) - potęgowanie
# potęgę mozna tez zrobić za pomocą **
# pi - liczba pi
# sqrt - pierwiastek kwadratowy
# wzor na pole kola - pi * r^2
# round(co, do ilu miejsc po przecinku) - zaokrąglenie do określonej liczby miejsc po przecinku


# oblicz pole kola sposob 1

promien = 2
pole = math.pi * math.pow(promien,2)
print(f"Pole kola o promienu {promien} cm wynosi {round(pole,2)} cm2")




# oblicz pole kola sposob 2

promien = 2
pole = math.pi * promien**2
print(f"Pole kola o promienu {promien} cm wynosi {round(pole,2)} cm2")