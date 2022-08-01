a=[1,2]
b=[3,4]
#low level operations(indexing)
'''
a[0] = a[0] + 0.5

a[1] = a[1] + 0.5

total = a[0] + a[1]
'''
#print(total)
#4.0


#I want to swap the co-ordinates

'''
x = a[0]
y = a[1]

a[1] = x
a[0] = y

'''
#print(a)

#[2, 1]

# reset the co-ordinates to [0, 0]

'''
a[0]= 0
a[1]= 0

print(a)
'''

#[0, 0]
#**********************************************************************************************************************
                                                                    #__init__()

#__init__() the constructor of class
#It accepts the self-keyword as a first argument which allows accessing the attributes or method of the class.
# __init__ method is helping us to do that
# internally the data is stored inside the dict
# which will be created once the __init__ method is called
# __init__ is also called as constructor. It will be automatically called
# when you call the class to save the data or when you create an instance 
# of the class
#The __init__() function is called automatically every time the class is being used to create a new object.
#**********************************************************************************************************************

#**********************************************************************************************************************
                                                                        #self

#Self is the instance or data which is pointing to one or more dictionaries
#The parameterized constructor has multiple parameters along with the self.
#self parameter is a reference to the current instance of the class

#**********************************************************************************************************************

#Program - 1st

#Create a class

'''
class Point:
    def __init__(self, a, b):
        self.a = a #Instance variables self.a, self.b and a, b are the local variables
        self.b = b
   
# Saving the data inside the class
p1=Point(1,2)
p2=Point(3,4)
p3=Point(5,6)

# # see the dictionary where the data is stored
# # instance dictionaries
print(p1.__dict__)
print(p2.__dict__)
print(p3.__dict__)
'''
#O/p -
{'a': 1, 'b': 2}
{'a': 3, 'b': 4}
{'a': 5, 'b': 6}

  
#**********************************************************************************************************************

#Program - 2nd
#Manuplating the data contained inside a dictionary

#**********************************************************************************************************************
'''
class Point1:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def move(self,dx, dy):
        self.a = self.a + dx
        self.b = self.b + dy

# Saving the data inside the class
p1 = Point1(1,2)
p2 = Point1(3,4)
p3 = Point1(5,6)

#manuplating the data contained inside a dictionary
p1.move(1,1)
p2.move(2,2)
p3.move(3,3)

#See the dictionary where the data has been stored
#Instance dictionary
print(p1.__dict__)
print(p2.__dict__)
print(p3.__dict__)


O/p-
{'a': 2, 'b': 3}
{'a': 5, 'b': 6}
{'a': 8, 'b': 9}
'''
#***********************************************************************************************************************
#Program - 3rd
#Reset the values

'''
class Point2:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def reset(self):
        self.a = 0
        self.b = 0
    
p1 = Point2(3,2)
p2 = Point2(4,4)
p3 = Point2(5,5)

p1.reset()
p2.reset()
p3.reset()

print(p1.__dict__)
print(p2.__dict__)
print(p3.__dict__)

'''

#O/p-
'''
{'a': 0, 'b': 0}
{'a': 0, 'b': 0}
{'a': 0, 'b': 0}
'''

#***********************************************************************************************************************
#Program - 4th
# Sort the no. (Swap the two numbers )

'''
class Point3:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def sort(self):
        if self.a > self.b:
            temp = self.a
            self.a= self.b
            self.b = temp

p1 = Point3(2,1)
p2 = Point3(4,2)
p3 = Point3(3,5)
p1.sort()
print(p1.__dict__)
print(p2.__dict__)
print(p3.__dict__)

#O/p-
#{'a': 1, 'b': 2}
#{'a': 4, 'b': 2}
#{'a': 3, 'b': 5}
'''
#***********************************************************************************************************************
#Program - 5th - Addinng 2 no.
'''
class Point3:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def total(self):
        return self.a + self.b     
        

p1 = Point3(2,1)
p2 = Point3(4,2)
p3 = Point3(3,5)

print(p1.total())'''

#O/p -
#3

'''
{'a': 2, 'b': 1}
{'a': 4, 'b': 2}
{'a': 3, 'b': 5}
'''
    
#***********************************************************************************************************************       
#Program - 6th
#Calculator performing arithmetical operations
'''
class Calculator:
    def __init__(self, a, b):
        print(f"Calling __init__ method and saving {a} and {b}")
        self.a = a
        self.b = b
    def add(self):
        return self.a + self.b
    def sub(self):
        return self.a - self.b
    def mul(self):
        return self.a * self.b
    def div(self):
        return self.a / self.b

#Saving the data inside the calculator object(inside dict)
c1 = Calculator(10,20)
c2 = Calculator(1,2)
c3 = Calculator(15,25)

print("After Addition :" ,c1.add())
print('After Substraction :' ,c2.sub())
print('After Substraction :', c3.mul())
print('After division :', c1.div())
'''
#O/p-
#__init__ method has been called automatically during the execution of the program
'''
Calling __init__ method and saving 10 and 20
Calling __init__ method and saving 1 and 2
Calling __init__ method and saving 15 and 25
After Addition : 30
After Substraction : -1
After Substraction : 375
After division : 0.5
'''

#***********************************************************************************************************************       
#Program - 7th
#Employee details
'''
e1 = {"fname": "steve", "lname": "jobs", "pay": 1000}
e2 = {"fname": "bill", "lname": "gates", "pay": 2000}

class Employee:
    def __init__(self,fname,lname,pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
    def email(self):
        return f"{self.fname}.{self.lname}@company.com"
    def pay_hike(self,percentage_hike):
        hike_amount = self.pay * percentage_hike
        self.pay = self.pay + hike_amount
e1 = Employee("komal",'Awati',1000)
e2 = Employee('Neeta','Awati',2000000)

print(e1.email())
e2.pay_hike(.1)
print(e2.__dict__)
'''

#O/p -
'''
komal.Awati@company.com
{'fname': 'Neeta', 'lname': 'Awati', 'pay': 2200000.0}
'''
        
#***********************************************************************************************************************       
#Program - 8th
#Constructor overloading
#Constructor overloading means more than one constructor in a class with the same name but a different argument (parameter).
#Multiple constructors are not directly supported in Python. When multiple constructors are provided in the class, the latest one overrides the previous one.
#1st Way -
#Using Multiple Arguments to Overload Constructors in Python

'''
class Point4:
    # overloaded constructor can be achieved by 
    # having default valules to the arguments
    def __init__(self, a=0, b=0, c=0):
        self.a = a
        self.b = b
        self.c = c
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def add(self,a,b):
        return a+b
    #8

    
    def add(self):
        return self.a + self.b
         #4
     
        
p4 = Point4(2,2)
print(p4.add(4,4))
print(p4.add())#4
'''

#***********************************************************************************************************************       
#Program - 8th
#Constructor Overloading

'''
class Point:
    # overloaded constructor can be achieved by 
    # having default valules to the arguments
    def __init__(self, a=0, b=0, c=0): #Method Inside the class
        self.a = a
        self.b = b
        self.c = c
    
    def __init__(self, a, b): #Method Inside the class
        self.a = a
        self.b = b

    def add(self, a, b):
        return a + b #Method Outside the class
    

def add(a, b, c):#Method Outside the class
    return a + b + c

p1 = Point(2,2)
print(p1.__dict__)

#O/p-
#{'a': 2, 'b': 2}

p1 = Point(2,2)
print(p1.add(2,2))
print(p1.__dict__)

'''

#O/p-
#{'a': 2, 'b': 2}
#4
#{'a': 2, 'b': 2}




    
    

    
        
    




