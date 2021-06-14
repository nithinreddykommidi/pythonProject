*** Settings ***
Documentation   To know how to do list operations

*** Variables ***
@{NAMES} =   sriram    RAJU    Balu    RAMESH    222

*** Test Cases ***
List Operations
    #Log     ${NAMES}          ERROR
    Log    ${NAMES}[1:3]     ERROR


