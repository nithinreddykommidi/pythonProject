*** Settings ***
Documentation    To know how to use logical operations
Library    Collections

*** Variables ***
${ONE}    8

*** Test Cases ***
Logical Operations
    #Run Keyword If   4 >= 4 or ${ONE} == 9   Log    LOGICAL OR\n    WARN

    Run Keyword If   4 > 3 and ${ONE} == 8   Log    LOGICAL AND \n    WARN
