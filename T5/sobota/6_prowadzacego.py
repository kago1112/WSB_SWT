import converter_prow

kilometry = float(input("Podaj liczbe km: "))
mile = float(input("Podaj liczbe mil: "))

wynik_1 = round(converter_prow.km_na_mile(kilometry),2)
wynik_2 = round(converter_prow.mile_na_km(mile),2)

print(f"{kilometry} km to {wynik_1} mil")
print(f"{mile} mil to {wynik_2} kilometrow")