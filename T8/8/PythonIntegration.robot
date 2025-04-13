*** Settings ***
Library    MyLib.py

*** Test Cases ***
Test funkcji Python greet
    ${msg}=    Greet    Marcin    # wywołujemy funkcję greet z argumentem Marcin
    Should Be Equal    ${msg}    Hello, Marcin!

Test funkcji Python add
    ${result}=    Add    5    7
    Should Be Equal As Integers    ${result}    12

Python inline sample
    ${lista}=    Evaluate    [x*x for x in range(5)]
    Log    ${lista}    #powinno  pokazać 0, 1, 4, 9, 16]
    ${dict}=    Evaluate    {"a": 1, "b": 2}
    Log    ${dict}    # powinno pokazać {'a': 1, 'b': 2}
            # wyniki zobaczysz w raporcie
    ${random_mod}=    Evaluate    __import__('random').randint(1, 10)
    ${num}=    Evaluate    ${random_mod}
    # coś się tu zjebało, ja pierdole