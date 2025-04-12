from math_utils import add

def test_add_two_numbers():
    # testujemy, czy dodawanie  2+3 jest równe 5
    result = add(2, 3)
    assert result == 5, f"Expected 5 but got {result}"
