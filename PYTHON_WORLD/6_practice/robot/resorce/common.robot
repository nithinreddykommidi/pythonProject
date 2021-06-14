*** Settings ***
Documentation    resource file

*** Variables ***
${a}    10
#{b}    12

*** Keywords ***
Add
    [Arguments]    ${a}     ${b}
    ${c}    EVALUATE     ${a}+${b}
    LOG    ${c}     WARN