# Difference ways of constructing a string object
word="Hello"
word1=str("Hello")
word2='Hie'
word3="""Bye"""
print(word)
print(word1)
print(word2)
print(word3)


# Zero Length string or an empty string
word4=""
print(word4)

# Both single and double quotes in single sting
word2='Hie'
word3="""Bye"""
print(word)
print(word1)

# We can use Escape Charater as well
sentence="Hello Python! Komal's programming skills here"
print(sentence)


sentence1="Hello Python! Komal\'s programming skills here"
print(sentence1)

sent2="Hello Python3! Komal\"s programming skills here"
print(sent2)

# We can use either double backslash or prefix 'r' which stands for raw string or regular expression

path1="C:\\testing\\newfolder"
print(path1)

path2="C:\\testing\\newfolder"
print(path2)

print(r"C:\testing\newfolder")

# use Triple Quotes to represent a Multi-Line String
multi_line_string = '''Hello There..
Welcome to Python tutorials'''
print(multi_line_string)

# =========================================================
my = 'Hello World'
# ========================================================
# type is an inbuilt function, which returns the datatype of the
# variable or an object



"""
dir is an inbuilt function, which returns a list of attributes 
that are attached to the object.
"""


"""
we can get information about a function using in-built function help()
"""

# String Functions
# NOTE: ALL STRING FUNCTIONS RETURNS A NEW STRING AND WILL NOT MODIFY OR MUTATE THE EXISTING STRING.

#upper,lower,count,find,replace,split,rfind,split,replace,join,

print(len(my))
print(my.upper())
print(my.lower())
print(my.count("l"))
print(my.count("Hello"))
print(my.count("Hello1"))
print(my.find("Hello"))
print(my.find('W'))
print(my.find('Hello1'))
print(my.replace('Hello', 'Hi'))
print(my.replace('H', 'B'))
print(my.split(','))


my1 = '***************Hello world==================='

print(my.strip())


























