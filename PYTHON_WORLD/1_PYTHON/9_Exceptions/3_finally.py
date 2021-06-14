'''
1. finally block will execute both times when try block executed successfully or fail.
2. It is used to do cleanup process(Closing File, Killing process, close remote connections like that).
'''
try:
    fh = open('3_finally.py')
    print(fh.readline())
    print('12' + '13')
except:
    print(' Try block got failed')
else:
    print(' Else block ')
finally:
    fh.close()
    print(' Finally block ')

