
#**51 Write a program to update the tuple**
'''
t1 = (1, 2, 3, 4)
t2 = (100, 200, 300)
# o/p (1, 2, 3, 4, 100, 200, 300)
res = t1 + t2
print(res) #(1, 2, 3, 4, 100, 200, 300)
'''
#**52 Write a program to replace value present in nested dictionary.**
#d = {'a': 100, 'b': {'m': 'man', 'n': 'nose', 'o': 'ox', 'c': 'cat'}}
# Replace "nose" with "net"
'''
for k, v in d.items():
    if isinstance(v , dict):
        d[k]['n'] = 'net'
        print(d)
'''
#**53 Write a program to count the number of white spaces in a file.**
'''
    
with open(r'D:\PYTHON\python programs\info.txt') as file:
    count = 0
    for line in file:
        count += line.count(" ")
# print(count)  
  
print(count)
    
  
'''

#**54 Grouping anagrams.**
'''
from collections import defaultdict
words = ['eat', 'ate', 'tea', 'hello', 'silent', 'listen']
d = defaultdict(list)
for word in words:
    s = ''.join(sorted(word))
    d[s].append(word)
print(d)

'''   
        


#**55 What is the difference between defaultdict and normal dictionary.**

"""
Defaultdict
-----------
1. When each key is encountered for the first time, it will not be there in the mapping.
2. So an entry is automatically created with default value (an empty list in case of defaultdict of list and zero in case of defaultdict int).
3. When keys are encountered again, the look-up proceeds normally as like a normal dictionary.
4. So, in defaultdict, creation of key, initialisation will happen simultaneously. 

Normal Dictionary
------------------
1. In case of normal dictionary, if the key does not exist, "KeyError" is raised. 
2. In order to work on the value, first the key needs to be created and initialised.
"""

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
'''
#**59 Write a list comprehension to get a list of even numbers from 1-50**

even_nos1 = [num for num in range(1, 51) if num % 2 == 0]
print("Even numbers in the list: ", even_nos1)

#OR

# Python program to print even Numbers in a List
# list of numbers
list1 = [10, 21, 4, 45, 66, 93]
# using list comprehension
even_nos = [num for num in list1 if num % 2 == 0]
print("Even numbers in the list: ", even_nos)




#**60 Find the longest non-repeated substring in the below string**
sentence = 'python is a good programming language and programming is fun'
words = sentence.split()
longest = ""
for word in words:
    if len(word) > len(longest):
        if sentence.count(word) == 1:
            longest = word
print(longest) #language
    




'''

#**61 Write a program to find the duplicate elements in the list without using inbuilt functions**
list = ['apple', 'google', 'apple', 'yahoo', 'google']
new = []
for word in list:
    n = list.count(word)
    if n > 1 and word not in new:
        new.append(word)
print(new)


#**62 Write a program to count the number occurrences of each item in the list without using any inbuilt functions**
names = ['apple', 'google', 'apple', 'yahoo', 'google', 'facebook', 'gmail', 'yahoo']
d = {}
for name in names:
    if name in d:
        d[name] += 1
    else:
        d[name] = 1
print(d)
        
#{'apple': 2, 'google': 2, 'yahoo': 2, 'facebook': 1, 'gmail': 1

#**63 Write a function to check if the number is Prime**
num = 5
def isprime(num):
    for i in range(2, num +1):
        if num % i == 0:
            return f'{num} is a prime'
            break
    else:
            return f'{num} is not a prime'

print(isprime(num))

#**64 How to create a tuple of numbers from 0 to 10 using range function**

t = tuple(range(11))
print(t)

#**65 Write a program to find the largest number in the list without using any inbuilt functions**
numbers = [10, 20, 30, 40, 50]
largest = 0
for item in numbers:
    if item > largest:
        largest = item
print(largest)

#**66 Write a method that returns the last digit of an integer. For example, the call of get_last_digit(3572) should return 2.**
n = 3572
def get_last_digit(n):
    return n%10
print(get_last_digit(n))

#**67 Write a program to find most common words in a given list.**
words = [
'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the', 'eyes', "don't", 'look', 'around', 'the',
'eyes', 'look', 'into','my', 'eyes', "you're", 'under'
]
from collections import Counter
c = Counter(words)
print(c)
print(c.most_common())
'''
**68 Make a function named tail that takes a sequence (like a list, string, or tuple) and a number n and returns the last n elements from the given sequence, as a list.**

**69 Write function named is_perfect_square that accepts a number and returns True if it's a perfect square and False if it's not.**

**70 Write a program to get all the duplicate items and the number of times the item is repeated in the list.**
>>> names = ['apple', 'google', 'apple', 'yahoo', 'yahoo', 'facebook', 'apple', 'gmail', 'gmail', 'gmail', 'gmail']

**71 Write a program to count the number of occurrences of each word in a file.**

**72 Write a program to count the number of occurrences of vowels in a file.**

**73 Write a program to print all numeric values in a list**

items = ['apple', 1.2, 'google', '12.6', 26, '100']

**74 Triangle Patterns**

*         
* *       
* * *     
* * * *   
* * * * * 

        * 
      * * 
    * * * 
  * * * * 
* * * * * 

    *     
   * *    
  * * *   
 * * * *  
* * * * * 

* * * * * * 
* * * * * 
* * * * 
* * * 
* *   
*   

* * * * * * 
  * * * * * 
    * * * * 
      * * * 
        * * 
          * 

 * * * * * *
  * * * * * 
   * * * *  
    * * *   
     * *    
      * 

1    
12   
123  
1234 
12345

    1
   12
  123
 1234
12345

     1    
    1 2   
   1 2 3  
  1 2 3 4 
 1 2 3 4 5


**75 Write a program count the occurrence of a particular word in the file**

**76 Write a program to map a product to a company and build a dictionary with company and list of products pair**
>>> all_products = ['iPhone', 'Mac', 'Gmail', 'Maps', 'iWatch', 'Windows', 
                'iOS', 'Google Drive', 'One Drive']

>>> # Pre-defined products for different companies
>>> apple_products = {'iPhone', 'Mac', 'iWatch'}
>>> google_products = {'Gmail', 'Maps', 'Google Drive'}
>>> msft_products = {'Windows', 'One Drive'}

**77 Write a program to rotate items of the list**
>>> names = ["apple", "google", "yahoo", "gmail", "facebook", "flipkart", "amazon"]

**78 Write a program to rotate characters in a string**

**79 Write a program to count the number of white spaces in a given string**

**80 Write a program to print only non-repeated characters in a string**

**81 What is the difference between a list and a tuple**
```python
"""
1. The main difference between a list and a tuple is that list's are mutable and tuples are immutable.
2. Python over allocates memory for lists. The reason for over allocation of memory is to support append operation. 
Where as in tuples, memory is not over allocated, as tuples does not support append operation. 
(Since tuples are immutable, it does not support append operation). 
3. Tuples are more memory efficient than lists. (because in tuples no extra memory is allocated. It is fixed).
4. Tuples are negligibly faster than lists. 
"""
```
**82 Write a program to print all the consonants in a given string**

**83 Write a program to count the number of commented lines in a text file**

**84 Write a program to check if the year is leap year or not**
```python
>>> import calendar
>>> print(calendar.isleap(2012))
>>> True
>>> print(calendar.isleap(2013))
>>> False
>>> print(calendar.isleap(2016))
>>> True
```
**85 Liner Search**

**86 Difference between xrange and range**
```python
"""
python2- xrange
python3- range

1. xrange does not stop, start and step attributes. But range object has start, stop and step attributes.
  Python-3
  r = range(0, 10)
  r.start
  r.stop
  r.step
   
  r = xrange(0, 10)
  In Python-2 The above attributes are not supported.

2. range Object supports slicing! But xrange does not support slicing

3. range object has __contains__ method implemented. So it supports membership testing. 
   But xrange does not implement __contains__ method. 
   So Python will iterate over each and every item in the range xrange object until it finds a match. 
   (So if you are searching for a number in range is faster than xrange)

4. range will accept integer of any size. But xrange objects accepts integer size equivalent to C long!

**87 Write a program to count no of capital letters in a string**

**88 Write a program to get the below output**

* 
* * 
* 
* * * 
* 
* * * * 
* 
* * * * * 
```

**89 Write a program to get the below output**
```python
>>> a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
o/p:
>>> [1, 2]
    [3, 4]
    [5, 6]
    [7, 8]
    [9]
```
**90 Write a program to check if the elements in the second list is series of continuation of the items in the first list**
```python
a = [10, 12, 14, 16, 18]
b = [20, 22, 24, 26, 28]

a = [0, 5, 10, 15]
b = [20, 25, 30, 35, 40]

x = [10, 20, 30, 40]
y = [50, 40, 60, 70]

**91 What is the difference between append() and extend() method in list**

```python
"""
1. append() method appends one item at the end of the list.
2. extend() method appends all the items of the iterable to the end of the list.
3. Both append() and extend() method's mutates the existing list.

e.g. 
>>> a = [1, 2, 3]
>>> b = (4, 5, 6)
>>> a.extend(b)
>>> a
[1, 2, 3, 4, 5, 6]

>>> c = {7, 8, 9}
>>> a.extend(c)
>>> a
[1, 2, 3, 4, 5, 6, 8, 9, 7]

>>> d = {'a': 1, 'b': 2, 'c': 3}
>>> a.extend(d)
>>> a
[1, 2, 3, 4, 5, 6, 8, 9, 7, 'a', 'b', 'c']

The list "a" is getting mutated each time when it is extended.
"""
```
**92 Write a program to find the first repeating character in a string**

**93 Write a program to find the index of nth occurrence of a sub-string in a string**

>>> sentence = "hello world welcome to python hello hi how are you hello there"

>>> index_nth_occurance(sentence, 'hello', 3)
>>> Start Index: 51, End Index: 56

**94 Write a program to print prime numbers from 1 to 50**

**95 Write a program to sort a list which has mix of both odd and even numbers, the sorted list should have odd numbers first and then even numbers in sorted order**
>>> a = [3, 4, 1, 7, 2, 12, 8, 6, 9, 11]
>>> # o/p should be [1, 3, 7, 9, 11, 2, 4, 6, 8, 12]

**96 Write a program to sort a list which has mix of both odd and even numbers, in the sorted list, odd numbers should be in ascending order and even numbers should be in descending order**
>>> a = [3, 4, 1, 7, 2, 12, 8, 6, 9, 11]
>>> # o/p should be [1, 3, 7, 9, 11, 12, 8, 6, 4, 2]

**97 Write a program to count the number of occurrences of non-special characters in a given string**
>>> s = 'hello@world! welcome!!! Python$ hi how are you & where are you?'

**98 Grouping Flowers and Animals in the below list**
items = ['lotus-flower', 'lilly-flower', 'cat-animal', 'sunflower-flower', 'dog-animal']

**99 Grouping files with same extensions**
files = ['apple.txt', 'yahoo.pdf', 'gmail.pdf', 'google.txt', 'amazon.pdf', 'facebook.txt', 'flipkart.pdf']

**100 Filter only those characters except digits**
s = '@hello12world34welcome!123'
'''
