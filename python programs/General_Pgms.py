#print("Aai")
'''word = 'hello world'

print(word)
hello world'''


#Python program to add two numbers using function
'''def add_num(a,b):#function for addition ( Python def keyword is used to define a function)
    sum=a+b;
    return sum; #return value
num1=int(input("input the number one: "))#input from user for num1
num2=int(input("input the number two :"))#input from user for num2
print("The sum is",add_num(num1,num2))#call te function


OR

def add(a,b):
    sum=a+b
    return sum
#o/p -
#add(2,3)
#5

'''
#Python program to print hello for 5 times
'''
for i in range(5):
    print("Hello")

o/p -
Hello
Hello
Hello
Hello
Hello
'''
#Python program to print hello for 5 times but with no space
'''
for _ in range(5):
    print("Hello" , end="")

o/p - HelloHelloHelloHelloHello

'''

#Python program to print hello for 5 times but with comma

'''
for _ in range(5):
    print("Mom", end=",")
o/p - Mom,Mom,Mom,Mom,Mom,
'''

# welcome to Python's world
'''word='welcome to python's world'
SyntaxError: unterminated string literal (detected at line 1)'''


'''
word='welcome to Python\'s world'
print(word)
o/p-
welcome to Python's world
'''

# file_path
'''
file_path = "c:\new_release\testing\release1.2\soemthing.exe"
print(file_path)

o/p :
-c:
ew_release	esting
elease1.2\soemthing.exe'''

#r - regular expressions/raw string
'''
file_path = r"c:\new_release\testing\release1.2\soemthing.exe" #r indicates raw string
print(file_path)
o/p :
c:\new_release\testing\release1.2\soemthing.exe'''

#<class 'str'>
'''word = str("hello world")
print(word)

o/p-
hello world
type(word)
<class 'str'>'''

#dir - it will returns all the list of the methods which are under string(datatype or spcified built in class)

'''
word = "Hello World"
print(word)

o/p-

Hello World
word
'Hello World'
dir(word)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

'''

#Upper - Convert it from Lowercase into Uppercase
'''
word = "Hello World"
print(word.upper())
o/p-
HELLO WORLD
'''

#strip - it will removes the leading and terminating white spaces from the specified string
'''
word = "             Hello World           "
print(word.strip())

word1 = "Hello World           "
print(word1.strip())

o/p-
Hello World
Hello World

'''

#split - It will split the words according to the given delimeters
'''
sentence = "hello,world,welcome,to,python"
parts=sentence.split(",")
print(parts)
o/p-
['hello', 'world', 'welcome', 'to', 'python']

sentence1 = "hello,world,welcome,to,python"
print(sentence1.split("+"))
o/p-
['hello,world,welcome,to,python']'''



'''
o/p -
['hello', 'world', 'welcome', 'to', 'python']'''

'''
sentence = "hello|world|welcome|to|python"

sentence.split("|")
print(sentence)
'''

#len - it will returns the length of the String

'''
word="Hello"
print(word)
word.len()
o/p -

AttributeError: 'str' object has no attribute 'len'''

'''
word="Hello"
print(word)

o/p-
word
'Hello'
len(word)
5
'''


