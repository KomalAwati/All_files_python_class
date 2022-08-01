#Input : malayalam
#Output : Yes
'''
def isPalindrome(s):
    return s == s[::-1]

s = "malayalam"
ans = isPalindrome(s)
or
 
if ans:
    print("Yes")
else:
    print("No")

def palindrome(s):
    return (lambda s: s == s[::-1]))
print(map(palindrome, l))
'''
                            #Or
#Inline if conditon
'''
l =["mom", 'hello','malayalam']
palindrome = lamda string : f"{string} is palindrome" if string == string [::-1] else f[string}
print(list(map(palindrome, l)))

#Map - Acts like for loop

'''
#************************************************************************************************************************
#Program -

#O/p- [1**0,]

'''
l1= [1,2,3.4,5]
l2 =[0,1,4,6]

# Using normal function

def exponent(n1, n2):
   return n1 ** n2
#or

#Using lambda function
#lambda n1,n2:n1 ** n2

print(list(map(exponent, l1, l2))) # as we are passing 2 arguments i am passing 2 iterables

#o/p - will be stored in the map object
     #- it will map the lesser element
'''
#************************************************************************************************************************
#Program -

'''
l1= [1,2,3.4,5]
l2 =[0,1,4,6]
zip(11,12)
address
list(zip(11,12)) #traverse

Zip_longest - not a inbuilt class
from itertools import zip_longest

itertools is the module name
list

map with extra value
fillvalue by default is none

'''
            


#************************************************************************************************************************
#Program -
'''
list_ = list(range(1,21))

def evens(num):
    if num % 2 == 0:
        return num ** 2 #it will oly returns the non default value

print(list(map(evens, list_)))

O/p

[1, 2, 133.63359999999997, 15625]
[None, 4, None, 16, None, 36, None, 64, None, 100, None, 144, None, 196, None, 256, None, 324, None, 400]
'''
'''
it has to be map each and every item
map cannot filter

if ur fu ll return any default value, it will discard the default i/p, it will just bother abt d nd n-d value
filter - it ll chck the cdn 
u cannot work on any functionality
oly filtering it out i/ps
it will take oly bool true values
'''

#or
# Using filter
'''
list_ = list(range(1, 21))
def evens(num):
    if num % 2 == 0:
        return num ** 2
print(list(fiter(evens, list_)))
'''


#************************************************************************************************************************
#Program -
#O/p-
#['eve', 'alex', 'alexa']
'''
names = ['steve','eve','alex','john','alexa']

vowels = lambda name : name[0].lower() in 'aeiou'
print(list(filter(vowels,names)))
'''

#O/p-
#['eve', 'alex', 'alexa']


#************************************************************************************************************************
def repeat_n_times(n):
    def repeat(func):
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            return res
        return wrapper
    return repeat

@repeat_n_times(3)
def display():
    print("in display")

display()

@repeat_n_times(5)
def add(a,b):
    print(a + b)























