#Program - 1st
#Longest word

#method 1st - #Using built in method

#sentence =  'Python is a programming language'
#words = sentence.split()
'''
#sorted()

res = sorted(words, key = len)
'''

''''
res

res[-1]
res[0]

#Unpack
shortest, *rest(used for both packing and Unpack), longest =
** -  whnvr uh unpacking dictionary 
Typeerror

shortest

longest

#without using longest word

'''
#************************************************************************************************
#method 2nd- #normal program
#sentence =  'Python is a programming language'
#words = sentence.split()
'''
longest =  ""

for word in words:
    if len(word) > len(longest):
        longest = word
print(longest)
'''

#O/p -
#programming

#************************************************************************************************
#Program - 2nd
'''
sentence =  'Python is a programming language and programming is fun'
words = sentence.split()
longest = ""
for word in words:
    if len(word) > len(longest):
        longest = word  
print(longest)
'''
#O/p -
#programming

#or
'''
sentence =  'Python is a programming language and programming is fun'
words = sentence.split()
longest =  ""

for word in words:
    if len(word) > len(longest) and words.count == 1:
        longest = word
print(longest)
'''
#Error


#************************************************************************************************
#Program 3
#longest word and its length
'''
sentence = "Hi Komal here"
words = sentence.split()

d = {word : len(word) for word in words}

res = sorted(d.items(), key=lambda item : item[-1])


#O/p
#d
#{'Hi': 2, 'Komal': 5, 'here': 4}

res

res[-1]

min_, *rest, _max =res

min_

max__
'''

#************************************************************************************************
#Using count

string = 'hello world'
d = {}
for char in set(string):
    d[char] = string.count(char)
print(d)

#************************************************************************************************
#without using inbuilt method
'''
string = 'hello world'
d = {}
for char in string:
    if char not in d:
        d[char] = 1
    else:
        d[char] += 1
'''
#O/p -
#d
#{'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}

#************************************************************************************************     
#Using defaultdict()

'''
from collections import defaultdict
string = 'hello world'
dd = defaultdict(int)
for char in string:
    dd[char] += 1
'''
#O/p -
#dd
#defaultdict(<class 'int'>, {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1})

    
#************************************************************************************************ 
