*** settings ***
Documentation   To know how many options to run ro bobot file

Library    String

*** Variables ***
${ONE}     99
${TWO}     RRR

*** Test Cases **
Testcase:1
    ${str1}    Convert To Lower Case    ABC
    Sleep     0s
    Log    TestCase 1 ==> ${ONE} :: ${TWO}  WARN

Testcase:2
    Sleep     0s
    Log    TestCase 2    WARN

Add
    Sleep     0s
    Log    TCase 3    WARN


