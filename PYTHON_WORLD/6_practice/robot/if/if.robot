*** Settings ***
Documentation    statements

*** Test Cases ***
Rob
    RUN KEYWORD IF    2==0  Add
        ELSE IF     3==3    sub
        ELSE    last
    LOG    Test     WARN

*** Keywords ***
Add
    LOG    Added    ERROR

Sub
    LOG    Subtract     ERROR

Last
    LOG    LASTcase     ERROR