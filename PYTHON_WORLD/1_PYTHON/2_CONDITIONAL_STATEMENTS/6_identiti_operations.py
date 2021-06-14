'''
1. Identiti opertions are "is" and "is not"
2. Using identity operators we can check memory location of objects.
'''

#a = 10
#b = 10

#print(' A ID is :', id(a))
#print(' B ID is :', id(b))

#if a is b : print(' IS ')


l = [1,2,3]             # A1 --> [1,2,3]
l2 = l.copy()           # A2
l.append(4)

print(' L id is  : ', id(l), l)
print(' L2 id is : ', id(l2), l2)

if l is not l2 : print(' OK ')

