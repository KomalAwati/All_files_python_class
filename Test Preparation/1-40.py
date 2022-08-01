
#**31 How to get the elements that are in list b but not in list a**
a = [1, 2, 3] 
b = [1, 2, 3, 4]

for item in b:
    if item not in a:
        print(item)

#4    

#**32 A function takes variable number of positional arguments as input. How to check if the arguments that are passed are more than 5**
def fun1(*arg):
    if len(arg) > 5:
        return f'{arg} length is greater than 5'
    else:
        return f'{arg} length is lesser than 5'
#print(fun1(1,2,3,45))

#**33 Count the number of occurrences of "CRITICAL", "INFO" and "ERROR" lines in a log file.**
# Assume Below is the contents of the log file

lines = """CRITICAL:Hello world
INFO: This is an info
ERROR: This is an error 
CRITICAL: This is critical
CRITICAL:Hello world
INFO: This is an info
ERROR: This is an error 
CRITICAL: This is critical
CRITICAL:Hello world
INFO: This is an info
ERROR: This is an error 
CRITICAL: This is critical
CRITICAL:Hello world
INFO: This is an info
ERROR: This is an error 
CRITICAL: This is critical"""

from collections import defaultdict
d = defaultdict(int)
for line in lines.split('\n'):
    word, other = line.strip().split(':')
    print(word,other)
    d[word]+=1
print(d)
    
#defaultdict(<class 'int'>, {'CRITICAL': 8, 'INFO': 4, 'ERROR': 4})


#**34 Write a function to reverse any iterable without using reverse function.
l = [1,2,3,4]
print(l[::-1])

#**35 Write a function to print the below output.**

# func("TRACXN", 0)  # Should print RCN
# func("TRACXN", 1)  # Should print TAX
def func(string, num):
    if num == 0:
        return string[1::2]
    elif num == 1:
        return string[::2]
print(func("TRACXN", 0))
print(func("TRACXN", 1))

#**36 Sum all the numbers in the below string.**
s = "Sony12India567Pvt2ltd"

total = 0
for char in s:
    if char.isdigit():
        total += int(char)
print(total) #23

#**37 Write a program to sum all the numbers in below string.**
s = "Sony12India567Pvt2ltd" # eg.12+567+2
total =0
num = 0
for item in s:
    if item.isdigit():
        num = num*10 + int(item)
    else:
        total += num
        num = 0
print(total + num)

#**38 Print all the numbers in the below list**
a = ['abc', '123', 'hello', '23']
for item in a:
    if item.isnumeric():
        print(item)

#**39 Program to print the number of occurrences of characters in a String without using inbuilt functions.**



import re
s = 'helloworld'
rr = re.findall(r'[\d]+', s)
print(rr)
#40 Program to print only the repeated characters and count of the same.**

