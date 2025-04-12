*** Variables ***
${USER}=    Kasia

*** Test Cases ***
Test zmiennej
    Log to Console    Uzytkownik: ${USER}
    Should be Equal as Strings    ${USER}    Kasia