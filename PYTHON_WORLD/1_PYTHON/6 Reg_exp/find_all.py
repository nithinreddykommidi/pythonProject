'''
1. Using findall we can search all matching pattrens in a string
2. It will return all matching values in list format
'''
import re

s = '345sri89ram99yes9678'

v = re.findall('[a-z]+', s)
print(v)
