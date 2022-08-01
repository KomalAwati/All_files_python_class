#Program - 1st
#WAP that takes variable number of positional argument as i/p how to check if the arguments that are passed are more than 5
'''
def vari(*args):
    if len(args) > 5:
        return f'the given positional arg :{args}'
    else:
        return f'the given positional {args} are less than 5'
print(vari(1,2,3,4,5,6))
'''

#***********************************************************************************************
#Program - 2nd
## WAF TO PRINT THE BELOW O/P
    #func('TRACXN',0)  # SHOULD PRINT RCN
    #func('TRACXN',1)  #SHOULD PRINT TAX
'''
def func(string, value):
    if value == 0:
        return string[1::2]
    if value == 1:
        return string[::2]
print(func('TRACXN',0)) 
print(func('TRACXN',1))
'''
#O/p =
'''
RCN
TAX
'''
#***********************************************************************************************
#Prime numbers are natural numbers that are divisible by only 1 and the number itself. In other words,
#prime numbers are positive integers greater than 1 with exactly two factors,
#1 and the number itself. Some of the prime numbers include 2, 3, 5, 7, 11, 13, etc.
'''
def prime(n):
    for i in range(2, n):
        if n % i == 0:
            return f'{n} is not prime'
        return f'{n} is prime '
print(prime(8))
'''
#7 is prime
#8 is not prime

 
#******************************************************************************************************
#Program - 4th
#Write a method that returns the last digit of an integer. for eg. the call of get_last_digit(3572) should return 2
'''
def get_last_digit(n):
    return n % 10
res = get_last_digit(3572)
print(res) # 2
'''
'''
def get_last_digit(num):
    converted_num = str(num)
    return converted_num[-1::]

print(get_last_digit('3572'))''' #2

#******************************************************************************************************
#Make a function named tail that takes a sequence (like a list , string or tuple) and a number n and returns the last n elements from
#  the given sequence as a list
'''
def tail(sequence, n):
    return (list(sequence)[-n : ])
print(tail('Hello', 2))
'''
#O/p-
#['l', 'o']

#******************************************************************************************************
#Program - 7
#Write a function which returns the sum of lengths of all the iterables
'''
l = (1,2,3,4,5)
t = (2,3,4)

def sum(l1, t1):
    return len(l1) + len(t1)
print(sum(l, t)) #8
'''

#******************************************************************************************************
#Python program to check whether a number is  prime or not

n = 5
if n > 1:
    for i in range(2, n):
        if n % i == 0:
            print("not prime")
    print("prime")            
        
     

#******************************************************************************************************
#Program - 9
#Python program to how to check if a given number is Fibonacci number
#Print 10th Fibonacci no.
n = 10
a, b = 0, 1
for i in range(n-1):
    c = a + b
    a, b = b, c
    print(a)

#O/p -
'''
1
1
2
3
5
8
13
21
34
'''

#Given n is fibonacci r not
def fibo(number):
    a = 0
    b = 1
    while a <= number:
        if a == number:
            return f'{number} is a fibonacci number'
        c = a + b
        a, b = b,c 
    else:
        return f'{number} is not a fibonacci number'
            
print(fibo(13))
print(fibo(9))
#O/p -
'''
13 is a fibonacci number
9 is not a fibonacci number
'''
