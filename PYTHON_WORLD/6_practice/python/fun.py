def fun(a,b,c):
    s = a+b+c
    print(s)
    
fun(20,c = 2, b = 5)


def ar(a,b,*c):
    print("a" ,a)
    print("b" ,b)
    print("c" ,c)
    
    
ar(1, 2, 3,4,5,6)

def kw(a,b,*c,**d):
    print("a" ,a)
    print("b" ,b)
    print("c" ,c)
    print("d" ,d)
   
    
    
kw(1, 2, 3,4,5,6,name = 'nithin',age = 25)

print('age', age)