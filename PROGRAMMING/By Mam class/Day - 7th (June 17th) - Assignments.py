#1. "Building a dict of word and length pair
#words = "This is a bunch of words"
'''
words = "This is a bunch of words"
l = words.split()
d = {}
for word in l:
    d[word] = len(word)
print(d) #{'This': 4, 'is': 2, 'a': 1, 'bunch': 5, 'of': 2, 'words': 5}
'''
#Comprehension
#d1 = {word : len(word) for word in l}
#print(d1) #{'This': 4, 'is': 2, 'a': 1, 'bunch': 5, 'of': 2, 'words': 5}

#***********************************************************************************************
#2. Flipping keys and values of the dictionary using dict comprehension
'''
d = {'a': 1, 'b': 2, 'c': 3}

d1 ={}

for key, value in d.items():
    d1[value] = key
print(d1)
'''
#{1: 'a', 2: 'b', 3: 'c'}

#Dict Comprehension
#d2 = {value : key for key.value in d.items()}
#print(d2)

#***********************************************************************************************
#3. Counting the number of each character in a String


#Using Normal Program
#my_string = 'guido van rossum'
'''
my_string = 'guido van rossum'
d ={}

for ch in my_string:
    if ch in d:
        d[ch] += 1
    else:
        d[ch] = 1
print(d)
'''
#O/p - {'g': 1, 'u': 2, 'i': 1, 'd': 1, 'o': 2, ' ': 2, 'v': 1, 'a': 1, 'n': 1, 'r': 1, 's': 2, 'm': 1}

#Using Normal #Using Normal Program
#when you try to access or modify a key that's not present in the dictionary, a default value is automatically given to that key .
#dict
#Just we are initializing the value
#0 false ()
#range and xrange

'''
from collections import defaultdict

string = 'guido van rossum'
dd = defaultdict(int)
for ch in string:
    dd[ch] +=1
print(dd)
'''
#you cannot update the values and u cnt use the loop in Comprehension


#Dict Comprehension
#string = 'guido van rossum'
#d1 = {ch:string.count(ch) for ch in string}
#print(d1)

#***********************************************************************************************

#5. Dictionary of character and ascii value pairs
#s = 'abcABC'
#Normal:
'''
s = 'abcABC'

d = {}

for ch in s:
    d[ch] = ord(ch)
print(d)'''
#{'a': 97, 'b': 98, 'c': 99, 'A': 65, 'B': 66, 'C': 67}

#Dict Comprehension
#d1 = {ch : ord(ch) for ch in s}
#print(d1) #{'a': 97, 'b': 98, 'c': 99, 'A': 65, 'B': 66, 'C': 67}

#***********************************************************************************************
#6. Creating Dictionary of city and population pairs using Dict Comprehension

#Normal:
'''
cities = ['Tokyo',
          'Delhi',
          'Shanghai',
          'Sao Paulo',
          'Mumbai'
          ]

population = ['38,001,000',
              '25,703,168',
              '23,740,778',
              '21,066,245',
              '21,042,538'
              ]
'''
    
#zip() function returns


#Dict Comprehension
#d = {cities : population for cities, population in zip(cities, population)}
#print(d)

#{'Tokyo': '38,001,000', 'Delhi': '25,703,168', 'Shanghai': '23,740,778', 'Sao Paulo': '21,066,245', 'Mumbai': '21,042,538'}

#***********************************************************************************************
#7. Create a dictionary of dialcode and country from the following list
'''
dial_codes = [
    (86, 'China'),
    (91, 'India'),
    (1, 'United States'),
    (62, 'Indonesia'),
    (55, 'Brazil'),
    (92, 'Pakistan'),
    (880, 'Bangladesh'),
    (234, 'Nigeria'),
    (7, 'Russia'),
    (81, 'Japan')
    ]
d = {}
for item in dial_codes: #unpack it
    key,value = item
    d[key] = value
print(d)
'''
#{86: 'China', 91: 'India', 1: 'United States', 62: 'Indonesia', 55: 'Brazil', 92: 'Pakistan', 880: 'Bangladesh', 234: 'Nigeria', 7: 'Russia', 81: 'Japan'}
#***********************************************************************************************

#8.  Left Triangle number Pattern
'''
    1
   12
  123
 1234
12345
'''

#Mam
'''
pat = ""
for row in range(1,6):
    pat = pat + str(row)
    print(f"{pat:>5}")
'''
#Qns by mam  - print 

#O/p -
"""
    1
   12
  123
 1234
12345
"""
#***********************************************************************************************

#10. 
'''
* 
* * 
* 
* * * 
* 
* * * * 
* 
* * * * *
'''

for row in range(2,6):
    print("*")
    print("* "*row)

'''
*
* * 
*
* * * 
*
* * * * 
*
* * * * * 

'''
#***********************************************************************************************
#11.
'''
1 2 3 *
1 2 * 4
1 * 3 4
* 2 3 4
'''
#1st way:
i = 4
for row in range(1,5):
    pat =""
    for j in range(1,5): #j=1,2,4
        if j == i:
            pat =pat + ' ' + '*'
            i -= 1
        else:
            pat = pat + " " +str(j)
    print(pat)

'''
1 2 3 *
1 2 * 4
1 * 3 4
* 2 3 4
'''
#2nd way:      
for i in range(1,5):
    for j in range(1,5):
        if i + j == 5:
            print("*", end =" ")
        else:
            print(j, end =" ")
    print()
    
'''
1 2 3 *
1 2 * 4
1 * 3 4
* 2 3 4
'''
#***********************************************************************************************
