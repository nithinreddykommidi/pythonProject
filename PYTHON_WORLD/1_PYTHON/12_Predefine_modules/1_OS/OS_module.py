'''
1. The OS module in python provides functions for interacting with the operating system. 
'''
import os

#print(dir(os))

# To create a directory
#os.mkdir('TODAY')

# To remove directory
#os.rmdir("TODAY")

# To create a file
#open("my_file.py", 'w')

# To rename a file 
#os.rename('my_file.py', 'RRR.py')

# To check file is exist or not return True is exist or False
#status = os.path.isfile('RRR1.py')
#print(' Status :', status)

# To run system commands
#print(os.system('dir'))
os.system('python today.py')
