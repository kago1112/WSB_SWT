import converter

#km na mile
km = float(input("Podaj liczbe kilometrow: "))
wynik_km = converter.km_na_mile(km)
print(round(wynik_km,2))

#mile na km
mile = float(input("Podaj liczbe mili: "))
wynik_mile = converter.mile_na_km(mile)
print(round(wynik_mile,2))