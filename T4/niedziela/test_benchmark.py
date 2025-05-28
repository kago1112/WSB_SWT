# nie wiem, kurwa, nie idzie ten test, a powinien, chuj mu  w dupe

# pytest benchmark to wtyczka do pytest, ktora nam automatycznie mierzy czas wykonywania testów
# więc w porównaniu z poprzednimi przykładami, tutaj nie musimy korzystać z funkcji start_time czy end_time

# wazne! - pytest sprawdza tylko pliki i funkcje zaczynajace sie od 'test'

# zainstaluj pytest-benchmark
# pip3 install pytest-benchmark


import time
import pytest

def slow_function():
    # funkcja ktora symuluje wolne dzialanie
    # tutaj usypiamy program na 0.5 sekundy
    time.sleep(0.5)
    return("Done")

# @pytest.mark.benchmark
def test_slow_function(benchmark):
    # funkcja, ktora przeprowadzi test sprawdzajacy ile srednio zajmuje wykonanie funkcji slow_function
    result = benchmark(slow_function)
    assert result == "Done"

# test odpalamy w terminalu
# pytest --benchmark-only test_benchmark.py

# wazne! - pytest sprawdza tylko pliki i funkcje zaczynajace sie od 'test'