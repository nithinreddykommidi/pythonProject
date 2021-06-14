'''
1. Search is used to find a patran any where in the string 
'''
import re

name = 'sriram123'
mo = re.search('\d+', name)
print(mo.group())



