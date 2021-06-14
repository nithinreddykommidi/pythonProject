'''
1. self is used to reffer the instance of the class to the method.
2. Based on self only the method will get to know for which instace it has to responce.
3. We can give any name in place of self.
'''
class One():
    def sub(self, a, b):
        print(' \n ID of self is : ', id(k))
        print(' \n A value is :', a)
        print(' \n A value is :', b)

ins1 = One()
ins2 = One()

#print(' \n ID of ins1 is  : ', id(ins1))
ins1.sub(10,5)
ins2.sub(100,200)





