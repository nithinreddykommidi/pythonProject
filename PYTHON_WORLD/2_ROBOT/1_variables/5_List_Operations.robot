*** Settings ***
Documentation   To know how to do list operations

Library    Collections


*** Test Cases ***
List Operations
    ${L}    Create List    11    22    33    44
    #log    List values are :: ${L}    WARN
    #Append To List    ${L}    55    66
    #log    List values are After APPEND :: ${L}    WARN

    #${R} =    Get From List    ${L}    2
    #log    Second index value :: ${R}    WARN

    #Remove From List    ${L}    -2
    #log    After removing based on index :: ${L}    ERROR

    Remove Values From List    ${L}    44    22
    log    After removing based on value ==> ${L}    WARN
