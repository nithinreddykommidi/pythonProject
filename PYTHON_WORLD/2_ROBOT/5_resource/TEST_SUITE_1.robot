*** Settings ***
Documentation   To know how to import resouce file

Resource    common_keywords.robot

*** Test Cases ***
Testcase:1
    Addition    5    5
    Log    ${NAME}    ERROR

