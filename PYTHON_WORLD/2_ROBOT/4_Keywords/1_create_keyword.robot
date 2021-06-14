*** Settings ***
Documentation    To know how to create keywords

*** Test Cases ***
#testcase:1
#    Addition

#testcase:2
#    Subtraction    9    5

testcase:3
    ${RV}     Multiplication    5    10
    Log       Multip OF 5 * 10 = ${RV}    ERROR

*** Keywords ***
Addition
    [Documentation]   Keyword without arguments
    ${SUM}    Evaluate    5 + 5
    Log    SUM OF 5 + 5 = ${SUM}    WARN

Subtraction
    [Arguments]    ${A}    ${B}
    [Documentation]   Keyword with arguments
    ${R}    Evaluate    ${A} - ${B}
    Log    Subtraction OF ${A} - ${B} = ${R}    WARN

Multiplication    [Arguments]    ${A}    ${B}
    [Documentation]    Keyword with RETURN
    ${R}    Evaluate    ${A} * ${B}
    [Return]    ${R}


