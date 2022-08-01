path = r'D:\PYTHON\Python Class\Day9 30th-31st May\access-log.txt'
#**1. Write a program to find the length of the string without using inbuilt function (len)**
'''
string = 'Komal'
count = 0
for _ in string:
    count += 1
print(count)
'''
#**2. Write a program to reverse a string without using any inbuilt functions.**
'''
string = 'Komal'
res = string[::-1]
print(res)
'''
'''
string= 'Hello Komal'
res = string.replace('Komal', 'Bmw')
print(res)
'''
#**3. Write a program to replace one string with another. e.g. "Hello World" replaces "World" with "Universe".**
'''
string = 'Hello World'
old = 'World'
new ='Universe'
res = ''
words = string.split()
for name in words:
    if name == old:
        res += new + " "
    else:
        res += name + " "
print(res)
'''

#**4. How to convert a string to a list and vice-versa.**
'''
string = 'Hello World'
words = string.split()
print(words)

res = " ".join(words)
print(res)
'''
#['Hello', 'World']
#Hello World


#**5. Convert the string "Hello welcome to Python" to a comma separated string.**
'''
string = "Hello welcome to Python"
words = string.split()
print(words)
res = ','.join(words)
print(res)
'''

#Hello,welcome,to,Python



#**6. Write a program to print alternate characters in a string.**
'''
string ='Komal'
res = string[::2]
print(res)
'''
#Kml


#**7. Write a Program to print ascii values of the characters present in a string.**
'''
string ='Komal'
for c in string:
    print(c, ord(c))
'''
'''
K 75
o 111
m 109
a 97
l 108
'''



#**8. Write a function to convert upper case to lower case and vice-versa without using inbuilt methods.**
'''
string1 = 'Hey'
def convert(string):
    res = []
    for char in string:
        temp = ord(char)
        if temp in range(97,123):
            res.append(chr(temp-32)) #97 -32 = 65 'here 65 is the 'A' ascii no.
        elif temp in range(65, 91):
            res.append(chr(temp + 32))
        else:
            res.append(temp)
    return ''.join(res)
print(convert(string1)) #hEY
'''

#**9. Write a program to swap two numbers without using the 3rd variable.**
'''
a = 10
b = 20

a,b = b,a

print('a =', a)
print('b =', b)
'''
#**10. Write a program to merge two different lists.**
'''
a = [1, 2, 3]
b = [4, 5, 6]

print([a + b])
print([*a, *b])
'''
#**11. Write a program to read a random line in a file. (ex. 50, 65, 78th line)**
'''
n = 6
from itertools import islice
with open (r'D:\PYTHON\Python Class\Day9 30th-31st May\access-log.txt') as file:
        lines = islice(file, n-1, n)
        print(list(lines))
'''
#**12. Write a program to read random lines in a file. (ex. I want read all lines 10th to 15th line)**
'''
start= 10
end = 16
from itertools import islice
with open (r'D:\PYTHON\Python Class\Day9 30th-31st May\access-log.txt') as file:
    lines = islice(file, start-1, end)
    print(list(lines))

'''
#13 Program to print the last "N" lines of a file.**
'''
path = r'D:\PYTHON\Python Class\Day9 30th-31st May\access-log.txt'
from collections import deque
n = 10
with open(path) as f:
    line = deque(f, n)
    print(line)

n = 6
from itertools import islice
with open (r'D:\PYTHON\Python Class\Day9 30th-31st May\access-log.txt') as file:
    lines_count = 0
    for _ in file:
        lines_count += 1
    print(lines_count)
    file.seek(0) #It will goes to the first charecters of in the file
    lines = islice(file, lines_count - n, lines_count)
    #(203 - 3 = 206, 203)
    print(list(lines))

'''
#**14. Write a program to check if the given string is Palindrome or not without using reversed method.**
'''
string1 = 'MOM'
def is_palindrome(string):
    rev_str = string[::-1]
    if string == rev_str:
        return True
    else:
        return False
print(is_palindrome(string1))
'''    

#**15 Write a program to search for a character in a given string and return the corresponding index.
'''
def search_character(string, key):
    for index, c in enumerate(string):
        if c == key:
            return f'Character {c} is at index {index}'
    
print(search_character('hello world', 'w'))
'''

#16. Write a program to get the below output
'''
sentence = "hello world welcome to python programming hi there"
#d = {'h': ['hello', 'hi'], 'w': ['world', 'welcome'], 't': ['to', 'there'], 'p': ['python', 'programming'] }
from collections import defaultdict
d = defaultdict(list)
words = sentence.split()
for word in words:
    d[word[0]].append(word)
print(d)
'''

#**17 Write a to replace all the characters with - if the character occurs more than once in a string**
#my_string = 'hellohai' # O/P should be '-e--o-ai'
'''
string = 'hellohai'
def rep(char):
    res = ''
    for char in string:
        if string.count(char) > 1:
            res += '-'
        else:
            res += char
    return res
print(rep(string))
'''
#**18 write a decorator that returns only positive values of subtraction**
'''
def positive(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return abs(result)
    return wrapper
@positive
def sub(a,b):
    return a - b
print(sub(3, 6)) #3
'''    


#**19 How to get the count of the number of instances of a class that is being created.**
'''
class Login:
    login_count = 0
    def __init__(self):
         Login.login_count += 1

'''

#**20 Write a function which takes a list of strings and integers.If the item is a string it should print as is and if the item is integer or float it should reverse it.**
'''
list = ['apple', 'yahoo', '1234', 100, 123.76, '26.23']
def spam(items):
    for item in items:
        if isinstance(item, str):
            print(item)
        else:
            temp = str(item)
            print(temp[::-1])
'''
#**21 Write a class named Simple and it should have iteration capability.**
'''
class Simple:
    def __init__(self, items):
        self._items = items
    def __iter__(self):
        return iter(self._items)
>>> s = Simple([1, 2, 3, 4, 5])
>>>
>>> for item in s:
print(item)
1
2
3
4
5
'''    

#**22 Write a Custom class which can access the values of dictionaries using d['a'] and d.a**


#**23 Write a python program to get the below output**
'''
string = "hai hello welcome"
words= string.split()
for word in words:
    print(word[::-1], end=" ")   #   iah olleh emoclew
print()
'''
#**24 Write a python program to get the below output**
'''
sentence = "Hi How are you" 
#o/p should be "ouy era woH iH"

res = sentence[::-1]
print(res)
'''

#**25 Write a lambda function to add two numbers (a, b)**
'''
res = lambda a,b : a + b
print(res(1,2))
'''


#**26 What is the output of the following**
'''
a = [1, 2, 3]
b = [4, 5, 6]
print([a, b])
print((a, b))
'''
'''

**27 How to remove duplicates from the list without using inbuilt functions**
>>> items = [1, 2, 3, 4, 1, 2, 3, 4, 5]

**28 Find the longest word in the sentence**

**29 write a program to reverse the values in the dictionary if the value is of type String**
>>> d = {'a': 'hello', 'b': 100, 'c': 10.1, 'd': 'world'}

**30 write a program to get 1234
t = ('1', '2', '3', '4')
'''
