# Decorator is a callable or func which adds some extra functionality to the existing function
# without modifying the existing or original function

#Program 1st - Division of two numbers and it doesn't matter in which sequence i am passing the values.
#Here it should be always numerator is bigger than the denominator
'''
def div(a,b):
    print(a/b)

def smart_div(func):
    def inner(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return inner

div = smart_div(div)
div(2,4)
'''
#O/p- 2.0
#***************************************************************************************************************************
                                                            #FUNCTIONS

#FUNCTIONS - ARE MAINLY USED TO PERFORM PARTICULAR TASK
'''
def f1():
    print('Called f1')
print(f1)#O/p ---------> o/p- <function f1 at 0x00000204591665F0>
f1() #O/p --------->o/p- Called f1'''

#NOTE : SINCE EVERYTHING IS AN OBJECT IN PYTHON WE CAN ABLE TO PASS f1 function into the program.
'''
def f2():
    print('called f2')

f2(f1)''' #O/p --------> TypeError: f2() takes 0 positional arguments but 1 was given
'''
def f2(arg_1):
    print('called f2')'''


#print(f2) # o/p----------------------------------------> <function f2 at 0x0000018E333B2560>
#f2(f1) #O/p --------> called f2
        #NOTE : BASICALLY HERE WE CAN WRITE A FUNCTION INSIDE ANOTHER FUNCTION
#print(f1) #O/p --------> <function f1 at 0x000001DB717265F0>
#f1() #O/p-----------> Called f1

#***************************************************************************************************************************

'''                                                           #WRAPPER FUNCTION
def f1(arg):
    def wrappper():
        print("started")
        arg()
        print("Ended")
    return wrappper'''

    # wrappper() #Actual function calling

    
'''
def f2():
    print('Hello')'''

#f1(f2) -----------------> nothing will print in the shell


#f1(f2)()    #PUTTING ANOTHER SET OF () #But this is the weired thing of calling the function
#----------------->
#o/p
#started
#Hello
#Ended

#print(f1(f2)) #---------------->#o/p- <function f1.<locals>.wrappper at 0x0000022A9DFC2560>
#f=f1(f2) #f1(arg)
#f()
#o/p
#started
#Hello
#Ended

#***************************************************************************************************************************
                                             #DECORATORS


#@f1  #-----------------> Does means Automatically f1() will be called indiactaes #f=f1(f2)
'''def f2():
    print('Hello')
f2()'''


#o/p
#started
#Hello
#Ended

#Adding parameters to function
'''
def f2(a):
    print(a)

f2("Hi")

 '''
'''
def f1(arg):
    def wrappper(*args,**kwargs):
        print("started")
        val=arg(*args,**kwargs)
        print("Ended")
        return val
    return wrappper
'''

'''
@f1
def f2(a,b=9):
    print(a,b)
f2('Hi!')
'''

#O/p-
#started
#Hi! 9
#Ended

'''
@f1
def add(x,y):
    return x+y
print(add(2,4))

'''
#O/p-
#started
#Hi! 9
#Ended
#started
#Ended



#***************************************************************************************************************************
    

                                                            #DECORATORS 

# Decorator is a callable or func which adds some extra functionality to the existing function
# without modifying the existing or original function

# Program1 - Adding extra functionality nd performing the mathematical operations

'''def log(func):
    # adding something extra to the original function or functionality or to the callback func
    def wrapper(*args, **kwargs):
        print(f"You are calling {func.__name__}") #Whenever i want to print a particular function name
        result = func(*args, **kwargs) # executing the callback function
        return result
    return wrapper'''

'''
@log        # spam = log(spam)
def spam():
    return "hello world"

@log    # greet = log(greet)
def greet(name):
    return f"hello {name}"

@log    # add = log(add)
def add(a, b):
    return a+b

@log        # sub = log(sub)
def sub(a, b, c):
    return a - b - c

@log    # mul = log(mul)
def mul(a, b, c, d):
    return a * b * c * d

'''

#print(mul(1,1,1,1))
#O/p -
#You are calling mul
#1


#print(add(10, 20))
#O/p -
#You are calling add
#30

#***************************************************************************************************************************
# Program 2 - Adding extra functionality and counting the time has taken to perform an operation

from time import sleep, time # NameError: name 'time' is not defined
                             #If we dont import the sleep ,time then it will throw an error
'''
def exe_time(func):
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print(f"Execution time: {end-start} seconds")
        return result
    return wrapper

@exe_time        # spam = exe_time(spam)
def spam():
    return "hello world"

print(spam) #o/p #--------------------> <function exe_time.<locals>.wrapper at 0x000001CF794025F0>
print(spam())'''

#O/p-
#Execution time: 0.0 seconds
#hello world


#***************************************************************************************************************************
# Program 3 - Using decorators print Hello world after the 5 secs
'''def delay(func):
    def wrapper(*args, **kwargs):
        sleep(5)        # extra functionality
        result = func(*args, **kwargs)
        return result
    return wrapper
@delay        # spam = delay(spam)
def spam():
    return "Hello world"
#print(spam)''' #O/P - <function delay.<locals>.wrapper at 0x000002147A952560>
#print(spam())

#O/p- NOTE: IT WILL WAIT FOR 5 SECS AND EXECUTE THE PROGRAM
#hello world 


#***************************************************************************************************************************
# Program 4 - Using decorators print a given string in the reverse order 

'''def reverse(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, str): #The isinstance() function returns True if the specified object is of the specified type, otherwise False.
            return result[::-1]
        else:
            return result
    return wrapper

@reverse        # spam = reverse(spam)
def spam():
    return "Hello world"
print(spam)''' #o/p- <function reverse.<locals>.wrapper at 0x0000020C881F2560>
#print(spam()) #O/p - dlrow olleH


#***************************************************************************************************************************

# Program 5 - Using Decorators perform add and sub operations but resulting value should be in positive form
'''def positive(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result < 0:
            return result * -1
        return result
    return wrapper'''

            #OR

'''
def positive(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return abs(result)'''  #Python abs() function is used to return the absolute value of a number,
                            #i.e., it will remove the negative sign of the number.
                            #The abs() takes only one argument, a number whose absolute value is to be returned.
                            #The argument can be an integer, a floating-point number, or a complex number.
   ' return wrapper'

'''
@positive
def add(a, b):
    return a+b

@positive
def sub(a, b):
    return a-b
'''

# print(add(3,2)) --------------------------> O/P - 5
#print(sub(6,4))  # --------------------------> O/P - 2
#print(sub(4,6)) #-------------------------->O/P - 2


#******************************************************************************************************************************


