*** Settings ***
Documentation   *  Provides a set of often needed generic keywords. Always automatically available without imports *

Library    Builtin

*** Variables ***
${name}    SRIRAM

*** Test Cases ***
Testcase:1
     #Log To Console    ${name}
     #Sleep    1s
     #Log    Name is = ${name}    WARN
     #Run Keyword If    3 == 3    Log    IF    ERROR
     Repeat Keyword    5    Log   SRIRAM    WARN

