from time import sleep,time
_cache={}

'''
def cache(func):
    def wrapper(*args,**kwargs):
        if args in _cache:
            return _cache[args]
        else:
            result = func(*args,**kwargs)
                #register that argument pair in dictionary
                _cache[args]=result
                return result
     return wrapper
     '''

'''
_cache={}

def cache(func):
    def wrapper(*args, **kwargs):
        if args in _cache:
            return _cache[args]
        else:
            result=func(*args,**kwargs)
            _cache[args]=result
            return result
    return wrapper

@cache
def add(a, b):
    return a+b

@cache
def sub(a, b):
    return a-b'''

#print(add(2,2))
#print(sub(4,2))

#O/p-
#4
#2

# count = {'add': 10, 'sub': 3, 'mul': 2, 'greet': 1}
'''
count = { }
def func_count(func):
    def wrapper(*args, **kwargs):
        function_name = func.__name__
        if function_name in count:
           count[function_name]  += 1
        else:
            count[function_name] = 1
        result = func(*args, **kwargs)
        return result
    return wrapper

@func_count
def add(a, b):
    return a+b

@func_count
def sub(a, b):
    return a-b'''

#print(add(2,2))
#print(sub(4,2))
#print(sub(4,2))

#O/p-
#4
#2
#2

'''
count = { }
def max_count(func):
    def wrapper(*args, **kwargs):
        function_name = func.__name__
        if function_name in count:
           count[function_name]  += 1
        else:
            count[function_name] = 1
        # check if the user is calling the function more than 5 times 
        # if the count is more than 5, raise exception
        if count[function_name] > 5:
            raise Exception("Max function call limit exceeded 5 times!!!")
        result = func(*args, **kwargs)
        return result
    return wrapper



@max_count
def sub(a, b):
    return a-b

print(sub(4,2))
print(sub(4,2))
print(sub(4,2))
print(sub(4,2))
print(sub(4,2))
print(sub(4,2))
'''


#O/p - Exception: Max function call limit exceeded 5 times!!!

'''
numbers = [ 1234567890, 9988776655, 1122334455, 910099887766 ]
def prefix_91(func):
    def wrapper(*args, **kwargs):
        # get that list out of the tuple
        temp = args[0]
        # check if each item of the list if prefixed with +91 or not
        # call the orginal func print_numbers and pass the updated list
        # new tuple with +91 prefixed
        args = (temp, )
        result = func(*args, **kwargs)      # args = ([12345, 343,45435], )
        return result
    return wrapper

@prefix_91
def print_numbers(numbers):
    for number in numbers:
        print(number)
    

'''
'''
l = [ 1234567890, 9988776655, 1122334455, 910099887766 ]
def wrapper(f):
    def fun(l):
        # complete the function
        # Standardize Mobile Number Using Decorators in python - Hacker Rank Solution START
        f(['+91 ' + c[-10:-5] + ' ' + c[-5:] for c in l])
        # Standardize Mobile Number Using Decorators in python - Hacker Rank Solution END
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)'''
   
#O/p-

'''sort_phone("1234567890")
+91  0
+91  1
+91  2
+91  3
+91  4
+91  5
+91  6
+91  7
+91  8
+91  9'''


#To write to a CSV file in Python, we can use the csv. writer() function.
#The csv. writer() function returns a writer object that converts the user's data into a delimited string.
'''
import csv  
for row in csv.reader(['num1, 123456789', 'num2, 987654321', 'num3, +23456789']):
    phoneNumber = row[1].strip()
    if not phoneNumber.startswith('+'):
        phoneNumber = '+' + phoneNumber
print(phoneNumber)
'''

#O/p-
#+23456789

'''
phone_numbers = ['12234', '91232324', '913746', '3453' '9145653', '95843']

for i, number in enumerate(phone_numbers):
    phone_numbers[i] = ''.join(['+', phone_numbers[i]]) if number.startswith('91') else phone_numbers[i]

'''

'''
def add_prefix(number):
    if len(str(number)) == 12 and str(number).startswith("91"):
        return "+" + str(number)[:2] + "-" + str(number)[2:]
    elif len(str(number)) == 10:
        return "+91-" + str(number)
    else:
        return number
    
def prefix_country_code(func):
    def wrapper(*args, **kwargs):
        numbers, = args
        prefix_numbers = [ add_prefix(number) for number in numbers ]
        return func(prefix_numbers)
    return wrapper

@prefix_country_code
def print_numbers(numbers):
    for number in numbers:
        print(number)
    

        
numbers = [ 1234567890, 9988776655, 1122334455, 910099887766, 11, 22, +911234567890,+9112345]

hello=print_numbers(numbers)'''

#O/p-
#+91-1234567890
#+91-9988776655
#+91-1122334455
#+91-0099887766
#11
#22
#+91-1234567890
#9112345



