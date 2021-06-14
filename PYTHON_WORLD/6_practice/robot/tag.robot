*** Settings ***
Documentation    TAGS

*** Test Cases ***
t1
    [Tags]    win
    LOG    t1   ERROR

t2
    [Tags]    win
    LOG    t2   ERROR

t3
    [Tags]    mac
    LOG    t3   ERROR

t4
    [Tags]    mac
    LOG    t4   ERROR
t5
    [Tags]    Linux
    LOG    t5   ERROR
t6
    [Tags]    Linux
    LOG    t6   ERROR
