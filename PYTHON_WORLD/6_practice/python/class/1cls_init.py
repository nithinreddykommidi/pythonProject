class One:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def year (self):
        print('age is', self.age)
        
    def st(self):
        print('name is' , self.name)
        
ins1 = One("nithin",25)
ins2 = One('naveen', 23)

ins1.st()