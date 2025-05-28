#symulujemy aplikacje, która działa WOLNO


import time

def slow_function():
    print("Rozpoczynam działanie slow_function...")
    time.sleep(3)  # symulacja wolnego działania, sleep opoznia nam egzekkucje funkcji o kilka sekund
    print("Zakończyłem działanie slow_function")

print("Zaczynam pomiar czasu")
start_time = time.time()  # pobieramy aktualny czas - czas rozpoczecia programu

slow_function()  # wywołujemy funkcję, która działa wolno

end_time = time.time()  # pobieramy czas po zakończeniu działania funkcji

elapsed_time = end_time - start_time  # obliczamy różnicę czasu
print(f"Funcja wykonała się w czasie {round(elapsed_time, 2)} sekund")  # wyświetlamy czas wykonania funkcji