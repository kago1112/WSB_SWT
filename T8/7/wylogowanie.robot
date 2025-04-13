*** Settings ***
Documentation    Testy logowania do aplikacji the-internet
Library    SeleniumLibrary

*** Variables ***
${LOGIN_URL}    https://the-internet.herokuapp.com/login
${BROWSER}    Chrome
${VALID_USERNAME}    tomsmith
${VALID_PASSWORD}    SuperSecretPassword!

*** Test Cases ***
LOGOWANIE I WYLOGOWANIE
    [Documentation]    Test logowania i wylogowania
    Open Browser    ${LOGIN_URL}    ${BROWSER}
    Wait Until Element Is Visible    id:username    timeout=8
    Input Text   id:username    ${VALID_USERNAME}
    Input Text   id:password    ${VALID_PASSWORD}
    Click Button    css:.radius
    Wait Until Element Is Visible    css:.flash.success
    Click Link    css:a.button.secondary.radius
    # coś do sprawdzenia, czy jesteśmy wylogowani, ale  popup window to w chuj utrudnia
    Close Browser
    