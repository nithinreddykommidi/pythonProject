'''
1. map is used to do operation on each iterable value and it will return all operations result in map object foramt.

2. Map taks two parameters one is function another one is iterable object

'''

## Map with def fucntion
def add(a):
    return  a + 10

#mo = map(add, (1,2,3,4,5,6))
#print(list(mo))

## Map with lambda function
mo = map(lambda a, b: a + b ,[1,2,3,4,5,6], [10,20,30,40])
print(tuple(mo))



