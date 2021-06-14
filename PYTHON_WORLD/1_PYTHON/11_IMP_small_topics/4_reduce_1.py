'''
1. reduce is used to do operation on each iterable value and its return all operations result sum.
2. reduce taks two parameters one is function another one is iterable object

'''

from functools import reduce

#(1+2)+3)+4)+5)

fib = reduce(lambda a,b: a + b,[1,2,3,4,5])
print(fib)

#fact = reduce(lambda a,b: a * b, [1,2,3,4,5])
#print(fact)





