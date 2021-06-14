*** Settings ***
Documentation    Loop operations using range function


*** Test Cases ***
Test For Loop
    FOR    ${INDEX}    IN RANGE    5    11    3
        log    ${INDEX}    WARN
    END

