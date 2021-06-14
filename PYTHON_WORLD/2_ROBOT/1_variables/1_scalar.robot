*** Settings ***
Documentation   To know how to do scalar operations

*** Variables ***
${NAME} =    Sri
${EID}     123

*** Test Cases ***
Scalar Operations
    Log    ${NAME}    WARN
