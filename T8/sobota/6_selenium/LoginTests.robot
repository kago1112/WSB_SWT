*** Settings ***
Documentation    Testy logowania do aplikacji the-internet
Library    SeleniumLibrary

*** Variables ***
${LOGIN_URL}    https://the-internet.herokuapp.com/login
${BROWSER}    Chrome
${VALID_USERNAME}    tomsmith
${VALID_PASSWORD}    SuperSecretPassword!
${INVALID_PASSWORD}    invalid_password

*** Test Cases ***
UDANE LOGOWANIE
    [Documentation]    Test logowania z poprawnymi danymi
    Open Browser    ${LOGIN_URL}    ${BROWSER}
    Wait Until Element Is Visible    id:username    timeout=8
    Input Text   id:username    ${VALID_USERNAME}
    Input Text   id:password    ${VALID_PASSWORD}
    Click Button    css:.radius
    Wait Until Element Is Visible   id:flash
    Close Browser

NIEUDANE LOGOWANIE
    [Documentation]    Test logowania z niepoprawnymi danymi
    Open Browser    ${LOGIN_URL}    ${BROWSER}
    Wait Until Element Is Visible    id:username    timeout=8
    Input Text   id:username    ${VALID_USERNAME}
    Input Text   id:password    ${INVALID_PASSWORD}
    Click Button    css:.radius
    Page Should Contain    Your password is invalid!
    Close Browser