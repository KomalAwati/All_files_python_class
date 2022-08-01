#Using print
'''def greeting():
     print("hello world")
     print('hello there')
     print("hello spam")
greeting()

o/p-
hello world
hello there
hello spam'''

#print(greeting()) you will not get proper o/p
#print(greeting()) we cannot call method in print statement whenever we are using print statements in the function


#Using return
'''
def greeting():
     return"hello world"
     return'hello there'
     return"hello spam"
print(greeting())

o/p -

hello world'''

#Note : We cannot use multiple return statements in the function body
#Note : A return statement is used to end the execution of the function call and “returns” the result (value of the expression following the return keyword) to the caller.
#Note: Return statement can not be used outside the function.

'''o/p -
hello world
hello there
hello spam
None'''


'''
def greet():
    return "hello world"
print(greet())

o/p-
hello world
'''

# greet() - if you will directly call the method in return statement it will not return any value
'''
def _greet(name):
    """ This function greets the user """
    return f"Hello {name}"
print(_greet('Komal'))

or

def _greet(name):
    return f'Hello {name}'
print(_greet('Komal'))
'''
# O/p-Hello Komal


#Addition of two numbers
'''
def add(a,b):
    return a+b
print(add(1,2))'''

#o/p - 3

#Passing the 3 arguments in the function

#Passing the by default values into the function
'''
def greeting(name, age, pay):
    print(f"Hello {name} you are {age} years of age and you get ${pay}")
greeting('Komal', 28,1000000)
'''
#o/p-
#Hello Komal you are 28 years of age and you get $1000000

'''
def student(UN,name,address):
    print(f"The Student UN is {UN} , her name is {name},her address is {address}")
student(3,'Komal','Sangli')
'''
#o/p-
#The Student UN is 3 , her name is Komal,her address is Sangli



#*************Using /,* into the function***************************
'''
def greet(name, /,*, reverse=True, debug=True):
    if debug:
        print("You called greet function ")
    if reverse:
        return f"hello {name[::-1]}"
    return f"Hello {name}"
print(greet('Komal')) # Hello lamoK
#greet("Komal") you don't need to call the again greet() here becouse we are using print statement in second line
'''

#o/p-
#You called greet function 
#hello lamoK


#***********************************Using /,* into the function**************************

#Program 1st - Using /,* into the function
'''
def greet(name,/,*,reverse=True, debug=True):
    if reverse:
        print(f"Hello {name[::-1]}")
    if debug:
        print("Function has been called successfully")
greet('Komal') '''
#o/p -
#Hello lamoK
#Function has been called successfully



#Program 2nd - Using /,* into the function
'''
def greeting(name, /, *, age, pay):
    print(f"Hello {name} you are {age} years of age and you get ${pay}")
greeting('Komal', age=20, pay=10000000)'''


#O/p -
# Hello Komal you are 20 years of age and you get $10000000

#NOTE - /,*- BEFORE THESE OPERATORS WE CAN ONLY PASS THE POSITIONAL ARGUMENTS
#NOTE - /,*- AFTER THESE OPERATORS WE CAN ONLY PASS THE KEYWORD ARGUMENTS

#*************************************************************************************************************************************



#************************Using * at the first argument in function********************
#Note - If we are specifying the * argument at the first in the function we should pass the value in the form of keyword arguments
#NOTE - *- AFTER THESE OPERATORS WE CAN ONLY PASS THE KEYWORD ARGUMENTS

#Program 1st - Using * at the first argument in function
'''def greeting(*, name, age, pay):
    print(f"Hello {name} you are {age} years of age and you get ${pay}")
greeting(name='Komal',age=28, pay=100000000)'''

#o/p -
#Hello Komal you are 20 years of age and you get $100000000
#greeting('Komal',28,10000000000000) -----------> TypeError: greeting() takes 0 positional arguments but 3 were given


#Program 2nd - Using * at the first argument in function

'''
def greet(*,name,pay):
    print(f"Hello {name} you pay is {pay}")
greet(name="Komal", pay=100000000)
'''

#O/p-
#Hello Komal you pay is 100000000

#*************************************************************************************************************************************
                                                            #SUMMARY

# add func can take any number of positional arguments from 0 to n
# * represents any number of positional arguments
# all the values will get collected inside a tuple
# * denotes variable number of positional arguments

#**************************************************************************************************************************************


##########################################Using *args#######################################################################################

#Program 1st - Using *args in the function
'''
def add(*args): # * represents any number of positional arguments
    total = 0
    for item in args:
        total = total + item
    return total
print(add(1,2,3,4)) 
'''
# O/p- 10

#Program 2nd - Using *args in the function
'''
def greet(*names):
    for name in names:
        print(f"Hello {name}")
greet('Komal') #Hello Komal
greet('Rani') #Hello Rani
greet('Teju','Sweetie','Bmw')
'''

#O/p-
'''Hello Teju
Hello Sweetie
Hello Bmw'''


###############################################################(Using *args, **kwargs)##################################################################################
#Program 1st - Using (*args, **kwargs) in the function

'''
def spam(*args, **kwargs):
    print(args)
    print(kwargs)
spam('Komal','Awati',name="Baby", Pay="10000000")'''


#o/p-
#('Komal', 'Awati')
#{'name': 'Baby', 'Pay': '10000000'}


#Program 2nd - Using (*args, **kwargs) in the function
'''
def greet(name, **info):
    print(f" Hello {name}")
    print(info)
    # for key, value in info.items():
    #     print(key, value)
greet('Komal', a=1, b=2)
'''

#0/p-
#Hello Komal
#{'a': 1, 'b': 2}

#*************************************************************************************************************************************
                                                            #SUMMARY

# *args - It can accept the any number of positional arguments and the data type will be 'tuple'
# **kwargs - It will accept any number of the keyword arguments and the data type will be 'dictionary'

#**************************************************************************************************************************************




###############################################################Using(**info),(a, *args),unpacking data,###################################################################
'''
def demo(**info):
    print(info)
demo(a=1,b=2,c=4,d=4)'''


#O/p-
# {'a': 1, 'b': 2, 'c': 4, 'd': 4}

'''
def func(a, *args):
    print(a)
    print(args)
func(10,2,3,4,5,6,7,8)
'''
#o/p-
#10
#(2, 3, 4, 5, 6, 7, 8)


# unpacking
'''
data = ("sandeep", 26, 1000)
_name, _age, _pay = data 
def greeting(name, age, pay):
    print(f"hello {name} you are {age} years of age and you get ${pay}")
greeting(_name, _age, _pay)
'''
#o/p-
#hello sandeep you are 26 years of age and you get $1000



# indexing
'''
data = ("sandeep", 26, 1000)
_name, _age, _pay = data
def greeting(name, age, pay):
    print(f"hello {name} you are {age} years of age and you get ${pay}")
greeting(data[0], data[1], data[2])'''
#o/p-
#hello sandeep you are 26 years of age and you get $1000


# pythonic approach
'''
data = ("sandeep", 26, 1000)
_name, _age, _pay = data 
def greeting(name, age, pay):
    print(f"hello {name} you are {age} years of age and you get ${pay}")
greeting(*data) '''    # unpacking greeting("sandeep", 26, 1000)
#o/p-
#hello sandeep you are 26 years of age and you get $1000


'''
d = { "name": "sandeep", "age": 26, "pay": 1000 }
def greeting(name, age, pay):
    print(f"hello {name} you are {age} years of age and you get ${pay}")
greeting( d['name'], d['age'], d['pay'] )
greeting(**d)  '''     # greeting(name="sandeep", age=26, pay=1000)
# greeting(fname="sandeep", age=26, pay=1000)

#o/p-
#hello sandeep you are 26 years of age and you get $1000
#hello sandeep you are 26 years of age and you get $1000




  




