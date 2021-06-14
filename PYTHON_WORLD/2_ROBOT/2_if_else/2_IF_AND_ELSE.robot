*** Settings ***
Documentation    To know how to do conditional operations

*** Test Cases ***
If And Else Statements
    Run Keyword If   5 >= 6    Add
    ...   ELSE IF    3 == 3    Log    First elif    WARN
    ...   ELSE IF    3 >= 6    Log    Second elif   WARN
    ...   ELSE       Log   Else block is     ERROR

*** Keywords ***
Add
    ${r}    Evaluate    45 + 5
    Log     SUM of 45 + 5 is ==> ${r}    ERROR
