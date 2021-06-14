'''
The elif statement allows you to check multiple expressions 
'''
sal = 750
if sal == 500:
    print(' \n If block ')
elif sal != 750:
    print(' \n First elif ')
elif sal > 800:
    print(' \n Second elif')
elif sal >= 750:
    print(' \n Third elif')
elif sal < 100:
    print(' \n Forth elif')
elif sal <= 50:
    print(' \n Fifth elif')
else:
    print(' \n Else block')