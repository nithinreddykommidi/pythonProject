*** Settings ***
Documentation   *  Library for generating, modifying and verifying strings *

Library    String

*** Variables ***
${name}         SRIRAM


*** Test Cases ***
Testcase:1
    #${name}    Convert To Lowercase    ${name}
    #Log    After Converting Lowercase ==> ${name}    ERROR

    #${FNAME}   Remove String    srikumar     sri
    #Log    After Removing SUB STRING ==> ${FNAME}    ERROR

    #${FULL_NAME}    Replace String    sriramsri    sri    RRR    1
    #Log    After Replace ==> ${FULL_NAME}    WARN

    #${SPLIT}    Split String    sri=ram=kumar    =
    #Log    After spliting ==> ${SPLIT}    ERROR

    ${SUBSTRING}    Get Substring    SRIRAM    0    3
    Log    Substring is ==> ${SUBSTRING}    WARN

