#Program - 1st
#1st way - Using By concatenation
#INPUT - string = 'Malayalam'
#OUTPUT - defaultdict(<class 'list'>, {'M': [0], 'a': [1, 3, 5, 7], 'l': [2, 6], 'y': [4], 'm': [8, 8]})

                                                    
                                                                                #Error
''' 
string = 'Hello'
d = {}
for index, char in enumerate(string):
    if char not in d:
        d[char] = index
    else:
        #d[char] = d[char] + index
        d[char].append(index)
'''

#O/p -
#d
#{'H': 0, 'e': 1, 'l': 5, 'o': 4}
#*************************************************************************************************
#OR
#2nd Way - Using By defaultdict 

'''
string = 'Malayalam'
from collections import defaultdict
dd = defaultdict(list)

for index,char in enumerate(string):
    dd[char] += [index]
dd[char].append(index)
print(dd)
'''
#O/p -
#defaultdict(<class 'list'>, {'M': [0], 'a': [1, 3, 5, 7], 'l': [2, 6], 'y': [4], 'm': [8, 8]})
#**************************************************************************************************
#Program - 2nd
#Write a program to create a dictionary of 1st charecter and the word starting with that first charecter pair in the given sentence

#INPUT 
#string_input = '''GeeksforGeeks is a Computer Science  portal for geeks.
       #It contains well written, well thought and well explained
       #computer science and programming articles, quizzes etc.'''
#OUTPUT -
#{'G': ['GeeksforGeeks'], 'i': ['is'], 'a': ['a', 'and', 'articles,'], 'C': ['Computer'], 'S': ['Science'], 'p': ['portal', 'programming'], 'f': ['for'], 'g': ['geeks.'], 'I': ['It'], 'c': ['contains', 'computer'], 'w': ['well', 'written,'], 't': ['thought'], 'e': ['explained', 'etc.'], 's': ['science'], 'q': ['quizzes']}


#ANS --

'''
# Declaring String Data
#string_input = 'GeeksforGeeks is a Computer Science  portal for geeks.'
  
# Storing words in the input as a list
words = string_input.split()
  
# Declaring empty dictionary
dictionary = {}
  
for word in words:
  
    # If key is not present in the dictionary then we
    # will add the key and word to the dictionary.
    if (word[0] not in dictionary.keys()):
  
        # Creating a sublist to store words with same
        # key value and adding it to the list.
        dictionary[word[0]] = []
        dictionary[word[0]].append(word)
  
    # If key is present then checking for the word
    else:
  
        # If word is not present in the sublist then
        # adding it to the sublist of the proper key
        # value
        if (word not in dictionary[word[0]]):
            dictionary[word[0]].append(word)
  
# Printing the dictionary
print(dictionary)
'''
#############
#O/p -


#**************************************************************************************************
                                                                                #OR
                                                                                #Error
#Without using inbuilt function
'''
words = 'Python is a programming language'
d ={}
for word in words:
    if word[0] not in d:
        d[word[0]] = [word]
    else:
        d[word[0]] += [word]
'''
#O/p -
#d
#{'P': ['P'], 'y': ['y'], 't': ['t'], 'h': ['h'], 'o': ['o', 'o'], 'n': ['n', 'n', 'n'], ' ': [' ', ' ', ' ', ' '], 'i': ['i', 'i'], 's': ['s'], 'a': ['a', 'a', 'a', 'a'], 'p': ['p'], 'r': ['r', 'r'], 'g': ['g', 'g', 'g', 'g'], 'm': ['m', 'm'], 'l': ['l'], 'u': ['u'], 'e': ['e']}

#******************************************************************************************************
                                                                                #OR
#defaultdict

'''
words = 'Python is a programming language'
from collections import defaultdict
dd = defaultdict(list)
words = words.split()

for word in words:
    dd[word[0]].append(word)

print(dd)

'''

#O/p -
#defaultdict(<class 'list'>, {'P': ['Python'], 'i': ['is'], 'a': ['a'], 'p': ['programming'], 'l': ['language']})

#******************************************************************************************************
#******************************************************************************************************
                                                                            #Anonymous function 

#By using normal function

'''
def square(num):
    return num ** 2
res = square(2)
print(res)
'''
#O/p -
#4

#Using lambda function
'''
square = lambda num: num ** 2

res = square(4)
print(res)
'''
#O/p -
#16

#******************************************************************************************************
#******************************************************************************************************
#Input  - [1,2,3,4]
#Output - [1,4,9.16]
                                                      #OR  #Using simple method
'''
number = [1,2,3,4]
square = lambda num : num ** 2
op = []
for n in number:
    res = square(n)
    op.append(res)
print(op)
'''
#O/p-
#[1, 4, 9, 16]

#******************************************************************************************************
                                                      #OR #USING MAP
#res = [(lambda x: x*x) (x) for x in range(5) ]
#print(res)

#O/p - [0, 1, 4, 9, 16]
#******************************************************************************************************
'''
square = lambda x: x ** 2
print(square(3))
'''
#******************************************************************************************************
#Or
'''
my_list = [1, 3, 5, 7]
for v in my_list:
    print (v**2)
'''
#O/p -
#1
#9
#25
#49
#******************************************************************************************************
                                                        #OR #BY USING MAP CLASS
'''
l = [1,2,3,4]
square = lambda num : num ** 2
res = map(square, l)
print(list(res))
'''

#O/p -
#[1, 4, 9, 16]
    
#******************************************************************************************************
#******************************************************************************************************
#Program - 1st
#O/p-
#['eve', 'alex', 'alexa']
'''
names = ['steve','eve','alex','john','alexa']

vowels = lambda name : name[0].lower() in 'aeiou'
print(list(filter(vowels,names)))
'''

#O/p-
#['eve', 'alex', 'alexa']
#******************************************************************************************************
#******************************************************************************************************
'''
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
'''

#O/p -
#in display
        
