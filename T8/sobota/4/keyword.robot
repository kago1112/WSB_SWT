*** Settings ***
Documentation    Test z keywordem z naszym imieniem

*** Variables ***
${imie}    Katarzyna
${nazwisko}    Golawska
${imie_i_nazwisko}    ${imie} ${nazwisko}

*** Test Cases ***
Ilosc znakow z imieniem Positive
    [Documentation]    Sprawdzenie, czy komunikat wyświetli nasze imie z var
    ${text}=    Set Variable    Hello, ${imie}!     #ustawiamy zmienną tekstową z naszym imieniem w var
    ${length}=    Evaluate    len("${text}")   #obliczamy długość tekstu
    Should Be Equal as Numbers    ${length}    17   #porównujemy długość z 17

Wyswietlenie komunikatu z Twoim imieniem
    [Documentation]    Sprawdzenie, czy komunikat wyświetli nasze imie z w konsoli
    ${length}=    Evaluate    len("${imie_i_nazwisko}")   #obliczamy długość tekstu
    Should Be Equal as Numbers    ${length}    18   #porównujemy długość z 18
    ${text}=    Set Variable    Hello, ${imie}. Your name and surname have ${length} characters.     #ustawiamy zmienną tekstową z naszym imieniem w var
    Log to Console    ${text}   #logujemy tekst do konsoli

