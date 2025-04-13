*** Settings ***
Documentation    Test for len function

** Test Cases ***
String Length Test Postive
    [Documentation]    Test the length of a string
    ${text}=    Set Variable    Hello, World!     #ustawiamy zmienną tekstową
    ${length}=    Evaluate    len("${text}")   #obliczamy długość tekstu
    Should Be Equal as Numbers    ${length}    13   #porównujemy długość z 13

String Length Test Negative
    [Documentation]    Test the length of a string
    ${text}=    Set Variable    Hello, World!     #ustawiamy zmienną tekstową
    ${length}=    Evaluate    len("${text}")   #obliczamy długość tekstu
    Should Be Equal as Numbers    ${length}    15   #porównujemy długość z 15 - niepoprawne