'''
1. Encapsulation is wrapping collection of methods together into single uint.

2. Using encapsulation we can give protection to the class attributes. Using access modifiers.
'''

class One():
    name = 'sriram'

    def add(self):
        print(' ADD is ')

    def sub(self):
        print(' SUB is:')


ins = One()

print('\n ', ins.name)
