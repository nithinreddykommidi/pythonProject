class One:
    def fun1(self):
        print("class1")

class Two(One):
    def fun2(self):
        print("class2")

class Three(Two):
    def fun3(self):
        print("class3")
        
        
 
        

ins1 = Three()
ins2 = Two()

ins1.fun1()
