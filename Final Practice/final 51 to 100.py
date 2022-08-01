#**51 Write a program to update the tuple**
t1 = (1, 2, 3, 4)
t2 = (100, 200, 300)
res = t1 + t2
print(res)
# o/p (1, 2, 3, 4, 100, 200, 300)

#**52 Write a program to replace value present in nested dictionary.**
d = {'a': 100, 'b': {'m': 'man', 'n': 'nose', 'o': 'ox', 'c': 'cat'}}
# Replace "nose" with "net"

for k, v in d.items():
    if isinstance(v, dict):
        d[k]['n'] = 'net'
        print(d)

#**53 Write a program to count the number of white spaces in a file.**

with open(r'D:\PYTHON\python programs\info.txt') as file:
    count = 0
    for line in file:
        count += line.count(' ')
print(count)
        
        

#**54 Grouping anagrams.**
words = ['eat', 'ate', 'tea', 'hello', 'silent', 'listen']

from collections import defaultdict

d = defaultdict(list)

for word in words:
    s = ''.join(sorted(word))
    d[s].append(word)
print(d)


#**55 What is the difference between defaultdict and normal dictionary.**
#**56 Explain property decorator in python.**

#**57 What is Mutable and Immutable datatypes.**

"""
1. Mutable datatypes are objects whose value can be changed after creation. e.g. list, dict, set, user defined classes.
2. Immutable datatypes are objects whose value can not be changed after creating. e.g. int, float, bool, tuple, namedtuple
"""

#**58 Explain get() method in dictionaries.**
"""
point =  {'a': 1, 'b': 2}
1. Values of dictionary can be accessed in two different ways. using square bracket syntax and the other one is using get() method.
2. When we try to access a key of a dictionary which does not exist using square bracket syntax (point['c']), "KeyError" exception is raised.
3. When we try to access a key of a dictionary which does not exist using get() method (point.get('c')), None is returned and no exception is raised.
4. We can pass a positional argument to get() method as custom message, so that get() method returns the custom message if the key does not exist.
           e.g. profile.get('c', 'Sorry the key does not exist')
"""

#**59 Write a list comprehension to get a list of even numbers from 1-50**\

l = [num for num in range(1, 51) if num%2 == 0]
print(l)

#**60 Find the longest non-repeated substring in the below string**
sentence = 'python is a good programming language and programming is fun'
words = sentence.split()
longest = ''
for word in words:
    if len(word) > len(longest):
        if sentence.count(word) == 1:
            longest = word
        
print(longest) #language
    
#**61 Write a program to find the duplicate elements in the list without using inbuilt functions**


#**62 Write a program to count the number occurrences of each item in the list without using any inbuilt functions**
names = ['apple', 'google', 'apple', 'yahoo', 'google', 'facebook', 'gmail', 'yahoo']

#**63 Write a function to check if the number is Prime**

#**64 How to create a tuple of numbers from 0 to 10 using range function**

#**65 Write a program to find the largest number in the list without using any inbuilt functions**
