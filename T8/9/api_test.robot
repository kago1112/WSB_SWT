*** Settings ***
Documentation    Nasz pierwszy test aplikacji API
Library    RequestsLibrary

*** Test Cases ***
Prykładowy GET na API
    [Documentation]    Test GET na API
    ${response}=    GET    https://jsonplaceholder.typicode.com/posts/1
    Should Be Equal    ${response}    200