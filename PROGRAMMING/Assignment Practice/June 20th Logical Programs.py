#1.
#A prime number is a positive integer that is divisible only by 1 and itself. For example: 2, 3, 5, 7, 11, 13, 17. 
#Number is prime or not
def isprime(num):
    for i in range(2, num):
        if i%2 == 0:
            return f'{num} is not a  prime '
        return f'{num} is a prime number'
print(isprime(20))

#*************************************************************************************************************
#2.
#WA method that returns the last digit of an integer for eg.the call of get_last_digit(3572)should return 2
def get_last_digit(num):
    return num%10
print(get_last_digit(3572)) #2  


#*************************************************************************************************************
#3
#Make a function named tail that takes a sequence (like a list , string or tuple) and a number n and returns the last n elements from
#  the given sequence as a list

def tail(sequence, n):
    return list(sequence [-n::])
print(tail('Hello', 2))

#['l', 'o']

#******************************************************************************************************
#4
#WAF named is_perfect_square that accepts a number and returns True if it's a perfect square and False if its not
def is_perfect_square(num):
    for i in range(0, num):
        if i * i == num:
            return True
    return False

print(is_perfect_square(4))
print(is_perfect_square(5))

#True
#False
#******************************************************************************************************
#5
#Write a function which returns the sum of lengths of all the iterables
l= [1,2,3,4]
t=(1,2,3,4)

def sum(l1, t1):
    return len(l1) + len(t1)
print(sum(l, t)) #8

#******************************************************************************************************
#6
#the integer sequence in which every number after the first two is the sum of the two preceding numbers. To simplify: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 
def fibo(n):
    a = 0
    b = 1
    while a <= n:
        if a == n:
            return f'{n} is fibo'
        c = a + b
        a, b = b, c    
    else:
        return f'{n} is not fibo'
print(fibo(3)) #3 is fibo

#******************************************************************************************************


