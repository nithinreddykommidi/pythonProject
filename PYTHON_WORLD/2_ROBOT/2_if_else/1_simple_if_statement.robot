*** Settings ***
Documentation    To know how to do conditional operations


*** Test Cases ***
IF Statement
    Run Keyword If    2 == 2    Addition

*** Keywords ***
Addition
    ${RV}    Evaluate    5 + 6
    log    \nAddition of 5 + 6 = ${RV}    WARN