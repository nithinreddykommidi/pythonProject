*** Settings ***
Documentation   strings and ints

*** Variables ***
${s}    'nithin'
${i}    123

*** Test Cases ***
Test
    Log     ${s} is string  WARN
    Log     ${i} is int     WARN