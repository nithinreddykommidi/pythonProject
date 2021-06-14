*** Settings ***
Documentation    tear

Suite Setup    Log      suite setup     ERROR
Suite Teardown    Log       Suite Teardown    ERROR

*** Test Cases ***
C1
    [Setup]    LOG    c1_setup  WARN
    LOG    c1   WARN
    [Teardown]    LOG    c1_tear    WARN

C2
    [Setup]    LOG    c2_setup  WARN
    LOG    C2   WARN
    [Teardown]    LOG    C2_Tear    WARN
