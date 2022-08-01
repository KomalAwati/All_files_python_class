'''from time import sleep
def greeting():
    print("Hello World")
    print("hello there")
    print("hello spam")
print(greeting())
#Hello World
#hello there
#hello spam

def greet():
    return 'hello world'

print(greet())
#hello world

def _greet(name):
    return f"Hello {name}"
print(_greet('Komal'))
# Hello Komal

def add(a,b):
    result = a + b
    return result
print(add(2,3))'''


'''
data = ("sandeep", 26, 1000)
_name, _age, _pay = data
def greeting(_name,_age,_pay):
    print(f"hello {_name} your {_age} and your {_pay}")
greeting(_name, _age, _pay)

o/p-
hello sandeep your 26 and your 1000'''
'''
data =("Komal", 28, 1000)
def greeting(_name,_age,_pay):
    print(f"hello {_name} your {_age} and your {_pay}")
print(greeting(data[0], data[1], data[2]))
'''

'''
data = ("sandeep", 26, 1000)
def greeting(name, age, pay):
    print(f"hello {name} you are {age} years of age and you get ${pay}")
greeting(data[0], data[1], data[2])'''

#o/p - hello sandeep you are 26 years of age and you get $1000

#hello sandeep you are 26 years of age and you get $1000

'''
data = ("sandeep", 26, 1000)
def greeting(name, age, pay):
    print(f"hello {name} you are {age} years of age and you get ${pay}")
greeting(*data) # it will unpack all the attribute value in pythonic way

'''


d = { "name": "sandeep", "age": 26, "pay": 1000 }
greeting( d['name'], d['age'], d['pay'] )
greeting(**d)
#o/p-
#hello sandeep you are 26 years of age and you get $1000






#o/p-
#greeting("Komal", 28,1000000000)
#hello Komal your 28 and your 1000000000



    




