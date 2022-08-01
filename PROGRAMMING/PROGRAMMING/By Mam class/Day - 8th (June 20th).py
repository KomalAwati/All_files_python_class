#Program - 1st
#WAP that takes variable number of positional argument as i/p how to check if the arguments that are passed are more than 5
'''
def pos_arg(*args): #positional argument
    if len(args) > 5:
        return f'the pos arguments are {len(args)}'
    else:
        print("the arguments are less than 5")
print(pos_arg(1,2,3,4,5,6))
'''
#o/p -
#the pos arguments are 6

#***********************************************************************************************
#Program - 2nd
## WAF TO PRINT THE BELOW O/P
    #func('TRACXN',0)  # SHOULD PRINT RCN
    #func('TRACXN',1)  #SHOULD PRINT TAX
'''
def func(string, value):
    #Using slicing
    if value == 0:
        print(string[1::2])
    elif value == 1:
        print(string[::2])
func('TRACXN',0)
func('TRACXN',1)
'''
#O/p -
#RCN
#TAX

#***********************************************************************************************

                                                                #Assignments

#Prime numbers are natural numbers that are divisible by only 1 and the number itself. In other words,
#prime numbers are positive integers greater than 1 with exactly two factors,
#1 and the number itself. Some of the prime numbers include 2, 3, 5, 7, 11, 13, etc.

#Program - 3rd
#Waf to check if the no. is prime or n?

'''
def isprime(num):
    if num > 1:
        for n in range(2,num):
            if num %n == 0:
                return f'{num} is not prime number'
        return f'{num} is prime number'
    
print(isprime(5)) #5 is prime number
'''

#******************************************************************************************************
#Program - 4th
#Write a method that returns the last digit of an integer. for eg. the call of get_last_digit(3572) should return 2

'''
# Find the last digit
def get_last_digit(n) :
    return n % 10
res = get_last_digit(3572)
print(res)

'''
  
#******************************************************************************************************
#Program - 5th
#Make a function named tail that takes a sequence (like a list , string or tuple) and a number n and returns the last n elements from
#  the given sequence as a list

# The length of the tail
'''
def tail(sequence, n):
    return list(sequence[-n :])
print(tail('hello',2))
'''

#OR
'''
def tail(sequence, n):
    return (sequence [-n :])
print(tail([1,2,3,4,5], 3))
'''
#O/p
#[3, 4, 5]
#******************************************************************************************************
#Program - 6th
#WAF named is_perfect_square that accepts a number and returns True if it's a perfect square and Fasle if its not
'''

def is_perfect_square(num):
    for i in range(0,num): # If you are not sure about the number then go and just mention num
        if i*i==num:
            return True
    else:
        return False
print(is_perfect_square(4))

'''

#******************************************************************************************************
#Program - 7
#Write a function which returns the sum of lengths of all the iterables
'''
l = [1,2,3,4,5]
t = (4,5,6)

def sum_of_lengths(l1, t1):
    return len(l1) + len(t1)
print(sum_of_lengths(l, t)) #8
'''

#******************************************************************************************************
#Program - 8
#Python program to check whether a number is  prime or not
'''
def isprime(num):
    if num > 1:
        for n in range(2,num):
            if num %n == 0:
                return f'{num} is not prime number'
        return f'{num} is prime number'
    
print(isprime(5)) #5 is prime number
'''
#******************************************************************************************************
#Program - 9
#Python program to how to check if a given number is Fibonacci number

#Fibonacci numbers - 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...
'''
n=8
c=0
a=1
b=1
if n==0 or n==1:
    print("Yes")
else:
    while c<n:
        c=a+b
        b=a
        a=c
    if c==n:
        print("Yes")
    else:
        print("No")
'''
#O/p -

#OR
'''
def fib(number):
    a = 0
    b = 1
    while (a <= number):
        if a  == number:
            return f'{number} is a fibonacci number'
        c = a + b
        a, b = b, c
    else:
        return f'{number} is not a fibonacci number'
print(fib(22))
'''
        
#O/p -19 is not a fibonacci number

#OR
num = 21

n1, n2 = 0, 1
sum = 0
if num <= 0:
    print('please enter a number greater than 0')
else:
    for i in range(0, num):
        print(sum, end= " ")
        n1 = n2
        n2 = sum
        sum = n1 +n2

