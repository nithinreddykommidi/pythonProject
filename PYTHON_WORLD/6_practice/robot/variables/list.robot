*** Settings ***
Documentation   list

*** Variables ***
@{lis}      'nithin',naveen,11,22

*** Test Cases ***
Test
    Log     @{lis} List    ERROR