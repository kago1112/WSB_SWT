from kod2 import fizzbuzz

def test_fizzbuzz_number():
    assert fizzbuzz(0) == None   # bo 0 nie jest przyjmowane przez fizzbuzz
    # assert fizzbuzz(0) == 0      -> wyjdzie error, bo 0 nie jest przyjmowane przez fizzbuzz
    assert fizzbuzz(1) == 1
    assert fizzbuzz(2) == 2
    assert fizzbuzz(19) == 19

def test_fizzbuzz_fizz():
    assert fizzbuzz(3) == "Fizz"
    assert fizzbuzz(6) == "Fizz"
    assert fizzbuzz(9) == "Fizz"

def test_fizzbuzz_buzz():
    assert fizzbuzz(5) == "Buzz"
    assert fizzbuzz(10) == "Buzz"
    assert fizzbuzz(35) == "Buzz"

def test_fizzbuzz_fizzbuzz():
    assert fizzbuzz(15) == "FizzBuzz"
    assert fizzbuzz(30) == "FizzBuzz"
    assert fizzbuzz(45) == "FizzBuzz"

def test_fizzbuzz_string():
    assert fizzbuzz("Mama") == None
    # assert fizzbuzz("5") == "Buzz"     -> wyjdzie error

def test_fizzbuzz_negative():
    assert fizzbuzz(-3) == None
    # assert fizzbuzz(-3) == -3   -> wyjdzie error, bo -3 nie jest przyjmowane przez fizzbuzz

def test_fizzbuzz_float():
    # assert fizzbuzz(5.7) == 5.7   error
    assert fizzbuzz(3.0) == "Fizz"