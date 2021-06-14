*** Settings ***
Documentation    keywors

*** Test Cases ***
rob
    argss


*** Keywords ***
add
    LOG    sub  WARN

sub
    [Arguments]    ${a}     ${b}
    LOG    EVALUATE ${a}+${b}   ERROR
argss
    [Arguments]    ${c}=10     ${d}=15
    LOG    evaluate ${c}+${d}    ERROR

