*** Setting ***
Library    SeleniumLibrary

*** Test Cases ***
Login facebook
    Open Browser    https://accounts.google.com/   Chrome
    Maximize Browser Window
    Sleep    5
    Input Text      identifierId    sriram.python111@gmail.com
    Sleep    5
    Click Element     //*[@id="identifierNext"]/span/span
    Sleep    5
    Input Text      password     Admin123
    Sleep    5
    Click Element     //*[@id="passwordNext"]/span/span
    Sleep    5
    Close Browser

