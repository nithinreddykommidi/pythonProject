'''
1. An abstract method is a method that is declared, but contains no implementation.
2. By defining an abstract base class, you can define a common API for a set of subclasses.
3. By using abc module we can define abstract class.
'''

from abc import ABCMeta, abstractmethod

class One(metaclass=ABCMeta):
    @abstractmethod
    def add(self):
        print(' \n ONE ADD ')

    @abstractmethod
    def sub(self):
        pass

## For abstract class we can not create instance
#a = One()
#a.add()

## If you inheritence an abstaruact class you should impliment that all those methods which are abstract ,methods
class Two(One):
    def add(self):
        print(" \n TWO ADD")

    def sub(self):
        print(' TWO SUB ')



ins = Two()
ins.add()
ins.sub()


