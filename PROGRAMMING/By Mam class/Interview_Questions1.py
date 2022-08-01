path = r'D:\PYTHON\Python Class\Day9 30th-31st May\access-log.txt'
#**1. Write a program to find the length of the string without using inbuilt function (len)**
'''
string = 'Komal'
count = 0
for _ in string:
    count += 1
print(count)#5

'''
#**2. Write a program to reverse a string without using any inbuilt functions.**
'''
string = 'Komal'
res = string[::-1]
print(res) #lamoK
'''

#**3. Write a program to replace one string with another. e.g. "Hello World" replaces "World" with "Universe".**
'''
string = 'Hello World'
old = 'World'
new = 'Universe'
res = ''
words = string.split()
print(words)
for word in words:
    if word == old:
        res += new + ' '
    else:
        res += word + ' '
print(res)

string = 'Hello World'
old = 'World'
new = 'Universe'
words = string.split()
for word in words:
    if word == old:
        print(word + ' ' + new)

'''
   

#**4. How to convert a string to a list and vice-versa.**
'''
string = 'Hello World'
words = string.split()
print(words)
res = ' '.join(words)
print(res)
'''

#**5. Convert the string "Hello welcome to Python" to a comma separated string.**
'''
string = 'Hello World'
words = string.split()
print(words)
res = ','.join(words)
print(res)
'''

#**6. Write a program to print alternate characters in a string.**
'''
string = 'Komal'
res = string[::2]
print(res) #Kml
'''
#**7. Write a Program to print ascii values of the characters present in a string.**
'''
string = 'Komal'
for char in string:
    print(ord(char))
'''

#**8. Write a function to convert upper case to lower case and vice-versa without using inbuilt methods.**
'''
def convert(string):
    res = []
    for char in string:
        temp = ord(char)
        if temp in range(97, 123):
            res.append(chr(temp - 32)) #LLO
        elif temp in range(65, 91):
            res.append(chr(temp + 32)) #he
    return "".join(res)
print(convert("HEllo"))
'''            
    
#**9. Write a program to swap two numbers without using the 3rd variable.**
'''
a = 10
b = 20

a, b = b, a

print(a)
print(b)
'''

#**10. Write a program to merge two different lists.**
'''
l1= [1,2,3]
l2 = [4,5,6]
res = l1 + l2
res1 = [*l1, *l2]
print(res)
print(res1)
'''
#**11. Write a program to read a random line in a file. (ex. 50, 65, 78th line)**
'''
from itertools import islice
n = 50
with open(path) as file:
    line = islice(file, n-1, n) 
    print(list(line))
'''

#**12. Write a program to read random lines in a file. (ex. I want read all lines 10th to 15th line)**
'''
start = 10
end = 15
from itertools import islice
with open(path) as f:
    lines = islice(f, start - 1, end)
    print(list(lines)) #print(lines) - it will provide us the address of the islice
'''

#**13 Program to print the last "N" lines of a file.**
'''
n = 10
from collections import deque
with open(path) as f:
    lines = deque(f, n)
    print(list(lines)) #print(lines) - will work
'''
    
#**14. Write a program to check if the given string is Palindrome or not without using reversed method.**

string = 'MOM'
#Note - string will traverse from the charecter vise but list of the items will traverse it from the word wise as we are checking the word is palindrome or not we can make use of the list
'''
def is_palindrome(string):
    words =  string.split()
    for word in words:
        rev_str = word[::-1]
    if string == rev_str:
        return f'{word} is palindrome'
    else:
        return f"{word} is not a palindrome"
print(is_palindrome(string))
'''

#**15 Write a program to search for a character in a given string and return the corresponding index.
#string = 'Hello dear'
'''
def is_char(string, key):
    for index, char in enumerate(string):
        if key == char:
            return f"{key} is at index of {index}"
        else:
            return f'{key} has not found in the given string'
print(is_char(string, 'z'))
'''

#16. Write a program to get the below output
'''
sentence = "hello world welcome to python programming hi there"
#d = {'h': ['hello', 'hi'], 'w': ['world', 'welcome'], 't': ['to', 'there'], 'p': ['python', 'programming'] }

words = sentence.split()
d = {}
for word in words:
    ch = word[0]
    if ch not in d:
        d[ch]=[]
    d[ch].append(word)
print(d)
            
#{'h': ['hello', 'hi'], 'w': ['world', 'welcome'], 't': ['to', 'there'], 'p': ['python', 'programming']}

'''



#**17 Write a to replace all the characters with - if the character occurs more than once in a string**
#my_string = 'hellohai' # O/P should be '-e--o-ai'
'''
string = 'hellohai'
for ch in string:
    if string.count(ch) > 1:
        print('-' , end= '')
    else:
        print(ch, end= '')
'''       
#-e--o-ai 


#**18 write a decorator that returns only positive values of subtraction**
'''
def positive(fun):
    def wrapper(*args, **kwargs):
        res = fun(*args, **kwargs)
        return abs(res)
    return wrapper

@positive
def sub(a, b):
    return a - b

print(sub(2,4))
'''
#2

#**19 How to get the count of the number of instances of a class that is being created.**

class Login:
    count = 0
    def __init__(self):
         Login.count += 1

      

#**20 Write a function which takes a list of strings and integers.If the item is a string it should print as is and if the item is integer or float it should reverse
#it.**
'''
list = ['Komal', 1234, 100, 20.5]
list1 = []
for item in list:
    if isinstance(item, str):
        print(item)
    else:
        temp = str(item)
        print(temp[::-1])
print(list)
'''

#**21 Write a class named Simple and it should have iteration capability.**
'''
class Simple:
    def __init__(self, item):
        self.item = item
    def __iter__(self):
        return iter(self.item)
s = Simple([1,2,3,4])
for i in s:
    print(i)

'''  

#**22 Write a Custom class which can access the values of dictionaries using d['a'] and d.a**
'''
class MyDict:
    def __init__(self,d):
        self._dict = d
    def __getitem__(self, item):
        return self._dict[item]
    def __getattr__(self, name):
        return self._dict[name]
d = MyDict({'a': 1, 'b': 2})
print(d.a) #__getattr__
print(d['b']) #__getitem__
'''

#**23 Write a python program to get the below output**

#sentence = "Hi How are you" 
#o/p should be "iH woH era uoy"
'''
sentence = "Hi How are you"
words = sentence.split()
for word in words:
    rev_word = word[::-1] 
    print(rev_word , end = ' ') #iH woH era uoy 
'''

#**24 Write a python program to get the below output**

#sentence = "Hi How are you" 
#o/p should be "ouy era woH iH"
'''
sentence = "Hi How are you"

rev_sentence = sentence[::-1]

print(rev_sentence)
'''
#uoy era woH iH

#**25 Write a lambda function to add two numbers (a, b)**
'''
res = lambda a, b : a + b
print(res(1,5))
'''
#6
#**26 What is the output of the following**
'''
a = [1, 2, 3]
b = [4, 5, 6]
print([a, b]) #[[1, 2, 3, 4, 5, 6]]
print((a, b)) #([1, 2, 3, 4, 5, 6])

'''

#**27 How to remove duplicates from the list without using inbuilt functions**
'''
items = [1, 2, 3, 4, 1, 2, 3, 4, 5]
list1 = []
for item in items:
    if item not in list1:
        list1.append(item)
print(list1)

'''
#[1, 2, 3, 4, 5]


#**28 Find the longest word in the sentence**
'''
sentence = "Hello world. Welcome to Python"
words = sentence.split()
longest = []
for word in words:
    if len(word) > len(longest):
        longest = word
print(longest)
'''
#Welcome

#**29 write a program to reverse the values in the dictionary if the value is of type String**
'''
d = {'a': 'hello', 'b': 100, 'c': 10.1, 'd': 'world'}

for key, value in d.items():
    if isinstance(value, str):
        d[key] = value[::-1]
    else:
        d[key] = value
print(d)
'''
#{'a': 'olleh', 'b': 100, 'c': 10.1, 'd': 'dlrow'}

#**30 write a program to get 1234
'''
t = ('1', '2', '3', '4')

res = ''.join(t)
print(res)
'''
#1234

#**31 How to get the elements that are in list b but not in list a**
'''
a = [1, 2, 3] 
b = [1, 2, 3, 4]

for item in b :
    if item not in a:
        print(item)

'''
#4


#**32 A function takes variable number of positional arguments as input. How to check if the arguments that are passed are more than 5**
'''
def args_pass(*args):
    if len(args) > 5:
        print('args are greater than 5')
    else:
        print('args are less than 5')
print(args_pass(1,2,3))

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
_errors = defaultdict(int)
for line in lines.split('\n'):
    error_type, other = line.strip().split(':')
    _errors[error_type] +=1
print(_errors) #defaultdict(<class 'int'>, {'CRITICAL': 8, 'INFO': 4, 'ERROR': 4})
    # Split the line based on newline character
# Split each line based on ":" to separate out error message part.







#**34 Write a function to reverse any iterable without using reverse function.

a = [1, 2, 3, 4, 5]
res2 = a[::-1]
print(res2)
    

#**35 Write a function to print the below output.**

# func("TRACXN", 0)  # Should print RCN
# func("TRACXN", 1)  # Should print TAX

def fun(string, num):
    if num == 0:
        return string[1::2]
    if num == 1:
        return string[::2]
        

print(fun("TRACXN", 0))
print(fun("TRACXN", 1))

#**36 Sum all the numbers in the below string.**
s = "Sony12India567Pvt2ltd"
total = 0
for item in s:
    if item.isdigit():
        total += int(item)
print(total) #2
        
**37 Write a program to sum all the numbers in below string.**
s = "Sony12India567Pvt2ltd" # eg.12+567+2
total = 0
num = 0
for num in s:
    if num.isdigit():
        
    

**38 Print all the numbers in the below list**
a = ['abc', '123', 'hello', '23']

**39 Program to print the number of occurrences of characters in a String without using inbuilt functions.**

**40 Program to print only the repeated characters and count of the same.**

'''
