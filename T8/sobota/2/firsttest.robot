*** Settings ***
Documentation    Pierwszy przykładowy test w Robot Framework

*** Test Cases ***
Hello World
    [Documentation]    Test sprawdza czy 2+2=4
    ${result}=    Evaluate    2+2     #oblicz 2+2 i zapisz wynik w zmiennej
    Should Be Equal As Integers    ${result}    4     #porownaj wynik z 4
