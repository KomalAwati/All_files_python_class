#Program - 1st
#  wap to create a dict of char and its index pair
'''
string = 'Malayalam'

d = {}

for index, char in enumerate(string):
    if char not in d:
        d[char] = [index]
    else:
        d[char] += [index]
print(d)
'''
#{'M': [0], 'a': [1, 3, 5, 7], 'l': [2, 6], 'y': [4], 'm': [8]}

#Using defaultdict
'''
from collections import defaultdict

dd = defaultdict(list)

for index , char in enumerate(string):
    dd[char] += [index]    
print(dd)
'''
#defaultdict(<class 'list'>, {'M': [0], 'a': [1, 3, 5, 7], 'l': [2, 6], 'y': [4], 'm': [8]})

#************************************************************************************************************************
#Program - 2nd
#  wap to create a dict of first char and the word starting with that first char pair
'''
string = 'hello world'

words = string.split()

d ={}

for word in words:
    if word[0] not in d:
        d[word[0]] = [word]
    else:
        d[word[0]] += [word]
print(d)
'''
#{'h': ['hello'], 'w': ['world']}

#Using defaultdict
'''
from collections import defaultdict

string = 'hello world'

dd = defaultdict(list)

for word in words:
    dd[word[0]].append(word)

print(dd)
'''
#defaultdict(<class 'list'>, {'h': ['hello'], 'w': ['world']})

#************************************************************************************************************************
#Program - 3rd
#  print square of number
'''
def square(num):
    return num ** 2
print(square(2)) #4
'''
#OR
#Using lambda fun
'''
square = lambda num: num ** 2
print(square(4))
print(square)   #return address
'''
#16

#************************************************************************************************************************
#Program - 4th
#INPUT - l = [1, 2, 3, 4, 5]
#O/P- [1, 4, 9, 16, 25]
'''
l = [1, 2, 3, 4, 5]

square = lambda num : num **2

ln = []

for number in l:
    res = square(number)
    ln.append(res)
print(ln)
'''
#Using Map function
'''
l = [1, 2, 3, 4, 5]
square = lambda num : num **2
res = map(square, l)
print(list(res))
'''

#************************************************************************************************************************
#Program - 5th
#Check list is palindrome or not

#Using lambda and map()
'''
lst= ['mom', 'help', 'malayalam']
palindrome = lambda string: f'{string} is palindrome' if string == string[::-1] else f'{string} is not palindrome'
res = list(map(palindrome,lst))
print(res)
'''
#['mom is palindrome', 'help is not palindrome', 'malayalam is palindrome']

#************************************************************************************************************************
#Program - 6th
#WAP to check even no between 1- 20

#Using filter
'''
list_ = list(range(1,21))
def evens(num):
    if num%2 == 0:
        return num ** 2
res = list(filter(evens, list_))
print(res)
'''
#[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

#The filter() function extracts elements from an iterable (list, tuple etc.) for which a function returns True.

#************************************************************************************************************************
#Program - 7th
#Wap to create a list of names starting with vowels
'''
names = ['steve','eve','alex','john','alexa']

vowels = lambda name : name[0].lower() in 'aeiou'
print(list(filter(vowels, names)))
'''
#['eve', 'alex', 'alexa']

#************************************************************************************************************************
#Program - 8th
#To find the len of iterable without using any inbuilt function
'''
string = 'TestYantra'
count = 0
for _ in string:
    count += 1
print(count)
'''
#O/p
#10
#************************************************************************************************************************
#Program - 9th
#WAP reverse a string without using any inbuilt method
#Using range:
'''
string = 'hello'
rev_str = string[::-1]
print(rev_str)
'''
#olleh

#or - By Mam
'''
string = 'hello'
rev_str = ''
for char in string:
    rev_str = char + rev_str
print(rev_str)
'''
#olleh

#************************************************************************************************************************
#Program - 10th
#WAP to replace one string with another

#method -1st - Without using inbuilt function
'''
s = 'hello world'
words = s.split()
old_word = 'world'
new_word = 'universe'
res = ""
for word in words:
    if word == old_word:
        res += new_word + " "
    else:
        res += word + " "
print(res)
'''

#O/p - 
#hello universe

#Or
'''
s = 'hello world'
print(s.replace('world', 'Universe'))
'''
#O/p - 
#hello universe

#************************************************************************************************************************
#Program - 11th
#WAP to convert string into list and vice versa
'''
# 1 converting string to list
#Method - 1st #Using Split()
string = 'hello world'

# 1 converting string to list
words = string.split()
print(words)

# 2
def convert(sents):
    return list(sents)

list_ = convert(words)
print(list_)#['hello', 'world']

# 3 converting list to string
def convert_list(lst):
    return " ".join(lst)

str_ = convert_list(words)
print(str_) #hello world

'''
#['hello', 'world']
#hello world
#************************************************************************************************************************
#Program - 12th
#Convert a string with seperated comma(',')

#string = 'hello welcome to python'
#  convert a string with seperated comma(',')

# 1
'''
words = string.split()
def comma_sep(words):
    return ",".join(words)

new_string = comma_sep(words)
'''
# print(new_string)

# 2  replace() method
# print(string.replace(' ', ','))

# 3  split - join
# print(",".join(words))

# 4 list()
#chars = list(string)
#print(chars)
#print(",".join(chars)) #h,e,l,l,o, ,w,e,l,c,o,m,e, ,t,o, ,p,y,t,h,o,n

#************************************************************************************************************************
#Program - 13th
# check given datatype is string or not
# 1
'''
def check_datatype(string):
    if isinstance(string, str):
        return True
    return False
print(check_datatype('hello'))   #  True
'''
# 2
'''
def check_dt(string):
    return isinstance(string, str)

print(check_dt(12546))  '''    #   False
    
#************************************************************************************************************************
#Program - 14th
#   swap the case of the given character

#  using in-built method
'''
def swap(char):
    if char.islower():
        return char.upper()
    elif char.isupper():
        return char.lower()

print(swap('a'))    #    A

#  without using in-built method
def swap_case(char):
    if ord("a") <= ord(char) <= ord("z"):
        print(chr(ord(char) - 32))
    elif ord("A") <= ord(char) <= ord("Z"):
        print(chr(ord(char) + 32))

swap_case("D")      #    d

'''
#************************************************************************************************************************
#Program - 14th
#  check if the given string is palindrome or not without using slicing method
'''
def palindrome(string):
    res = ""
    for char in string:
        res = char + res
    if res == string:
        return f"{string} is palindrome"
    return f"{string} is not palindrome"

print(palindrome("mom"))
'''
#************************************************************************************************************************
#Program - 15th

#   replace all vowels in the string to   *

'''
def replace(string):
    res = ""
    for char in  string:
        if char in "aeiou":
            res = res + "*"
        else:
            res = res + char
    return res

print(replace("hello world"))
'''

#    h*ll* w*rld

#************************************************************************************************************************
#Program - 15th

#   replace repeated char with  -
#   replace repeated char with  -
'''
def replace(string):
    res = ""
    for char in string:
        if string.count(char) > 1:
            res = res + "-"
        else:
            res = res + char
    return res

print(replace("hello world"))   #   he--- w-r-d
'''
#************************************************************************************************************************
#Program - 16th
#WAP to count each of the word in the given string
'''
sentence = "python is a good programming language"
words = sentence.split()
d={}
for word in words:
    d[word] = len(word)
print(d)
'''
#{'python': 6, 'is': 2, 'a': 1, 'good': 4, 'programming': 11, 'language': 8}
#using dictionary comprehension
'''
sentence = "python is a good programming language"
words = sentence.split()
d={word:len(word) for word in words}
print(d) #{'python': 6, 'is': 2, 'a': 1, 'good': 4, 'programming': 11, 'language': 8}
print(words[-2]) #programming
'''

#************************************************************************************************************************
#Program - 17th
#WAP to print longest word in the sentence
#  Normal program

sentence = "python is a good programming language"
words = sentence.split()
longest = ""
for word in words:
    if len(word) > len(longest):
        longest = word  
print(longest)

#Or #Using Sorted method
res = sorted(words, key = len)
# print(res)     #    ['a', 'is', 'good', 'python', 'language', 'programming']
sortest, *rest, longest = res #Unpacking
# print(sortest)
print(longest)

'''
