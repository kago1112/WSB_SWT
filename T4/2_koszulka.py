# CWICZENIE 2
# Napisz funkcję o nazwie koszulka(), która akceptuje rozmiar i tekst wiadomości, która powinna zostać wydrukowana na koszulce. 
# Funkcja powinna wydrukować zdanie podsumowujące rozmiar koszulki i wydrukowaną na niej wiadomość.
# Wywołaj funkcję raz, używając argumentów pozycyjnych, aby utworzyć koszulkę. Wywołaj funkcję drugi raz, używając argumentów 
# słów kluczowych, aby utworzyć koszulkę.

def koszulka(rozmiar, tekst_wiadomosci):
    print(f"Zamówiona koszulka ma rozmiar {rozmiar} z nadrukiem o treści {tekst_wiadomosci}")

koszulka("M", "andiamo")        #argumenty pozycyjne
koszulka(tekst_wiadomosci="andiamo", rozmiar="M")       # argumenty słów kluczowych

# Można również użyć argumentów mieszanych, np.:
koszulka("L", tekst_wiadomosci="hello world")  # mieszane argumenty