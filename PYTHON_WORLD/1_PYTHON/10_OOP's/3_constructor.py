## Using __init__ we can create constructor
## Using constructor we can create instance varables.
## Constructor method will call when calling class
class One:
    def __init__(self, name, eid):
        self.name = name
        self.eid  = eid
        print('__init__')

    def add(self):
        print(' Add ', self.name)

    def sub(self):
        print(' SUB ', self.name)
        print(' SUB EID ', self.eid)


inst = One('SRIRAM', 999)
inst.add()
#inst.sub()




