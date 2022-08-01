
from abc import ABC, abstractclassmethod

'''
Abstract classes are classes that contain one or more abstract methods. An abstract method is a method that is declared,
 but contains no implementation. Abstract classes may not be instantiated, and require subclasses to provide 
 implementations for the abstract methods.
'''
'''

# Class That can't be instantiated
class AbstractClassDemo(ABC):

    @abstractclassmethod
    def skills(self):
        print('Hello')


#abs = AbstractClassDemo()
## It though error as Abstract class can't be instantiated

class Base(AbstractClassDemo):
    def __init__(self):
        self.name = 'Sudhanshu Patel'
    def skills(self):
        print('I am in Base Class')

    def __del__(self):
        class_name = self.__class__.__name__
        print( class_name, 'Destroyed Successfully')


obj =  Base()
obj.skills()

'''
#I am in Base Class

class AbstractClassDemo:

    def skills(self):
        print('Hello')


abs = AbstractClassDemo()
## It though error as Abstract class can't be instantiated

class Base(AbstractClassDemo):
    def __init__(self):
        self.name = 'Sudhanshu Patel'
    def skills(self):
        print('I am in Base Class')
        super().skills()


obj =  Base()
obj.skills()
