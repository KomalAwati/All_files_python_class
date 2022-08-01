#Program -1st
'''
def fun1(fun):
    def wrapper():
        print('hello')
        fun()
        print('welcome to decorators')
    return wrapper
def fun2():
    print('pythonista')

fun2 = fun1(fun2)

fun2()

'''
#o/p -
'''
hello
pythonista
welcome to decorators
'''

#**********************************************************************************************************
'''
#OR
#Using decorators
def fun1(fun):
    def wrapper():
        print('Hello')
        fun()
        print('welcome to decorators')
    return wrapper
@fun1 #fun2 = fun1(fun2) , Pysyntax
def fun2():
    print('pythonista')

fun2()
'''
#**********************************************************************************************************

#Using decorators syntax

'''
def fun1(fun):
    def wrapper(*args, **kwargs):
        print('hello')
        fun(*args, **kwargs)
        print('Hey Complete the decorators')
    return wrapper
@fun1
def fun2():
    print('Bmw')

fun2()

'''
#**********************************************************************************************************
































