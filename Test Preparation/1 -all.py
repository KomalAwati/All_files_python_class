#**1. Write a program to find the length of the string without using inbuilt function (len)**

string = "Komal"
count = 0
for i in string:
    count += 1
print(count)

#5
#**2. Write a program to reverse a string without using any inbuilt functions.**
string = "Komal"

s = string[::-1]

print(s) #lamoK


##**3. Write a program to replace one string with another. e.g. "Hello World" replaces "World" with "Universe".**

string = 'Hello World'
old = 'World'
new = 'Universe'
words = string.split()
for word in words:
    if word == old:
        print(word + ' ' + new)

string = 'Hello WOrld'
old = 'world'
new = 'universe'




    
##**4. How to convert a string to a list and vice-versa.**

##**5. Convert the string "Hello welcome to Python" to a comma separated string.**

##**6. Write a program to print alternate characters in a string.**

##**7. Write a Program to print ascii values of the characters present in a string.**
##
##**8. Write a function to convert upper case to lower case and vice-versa without using inbuilt methods.**
##
##**9. Write a program to swap two numbers without using the 3rd variable.**
##
##**10. Write a program to merge two different lists.**
##
##**11. Write a program to read a random line in a file. (ex. 50, 65, 78th line)**
##
##**12. Write a program to read random lines in a file. (ex. I want read all lines 10th to 15th line)**
##
##**13 Program to print the last "N" lines of a file.**
##
##**14. Write a program to check if the given string is Palindrome or not without using reversed method.**
##
##**15 Write a program to search for a character in a given string and return the corresponding index.
##
##16. Write a program to get the below output
##sentence = "hello world welcome to python programming hi there"
##d = {'h': ['hello', 'hi'], 'w': ['world', 'welcome'], 't': ['to', 'there'], 'p': ['python', 'programming'] }
##
##**17 Write a to replace all the characters with - if the character occurs more than once in a string**
##```python
##my_string = 'hellohai' # O/P should be '-e--o-ai'
##
##**18 write a decorator that returns only positive values of subtraction**
##
##**19 How to get the count of the number of instances of a class that is being created.**
##
##**20 Write a function which takes a list of strings and integers.If the item is a string it should print as is and if the item is integer or float it should reverse it.**
##
##**21 Write a class named Simple and it should have iteration capability.**
##
##**22 Write a Custom class which can access the values of dictionaries using d['a'] and d.a**
##
##**23 Write a python program to get the below output**
##
##sentence = "Hi How are you" 
##o/p should be "iH woH era uoy"
##
##**24 Write a python program to get the below output**
##
##sentence = "Hi How are you" 
##o/p should be "ouy era woH iH"
##
##
##**25 Write a lambda function to add two numbers (a, b)**
##
##**26 What is the output of the following**
##
##a = [1, 2, 3]
##b = [4, 5, 6]
##print([a, b])
##print((a, b))
##
##**27 How to remove duplicates from the list without using inbuilt functions**
##>>> items = [1, 2, 3, 4, 1, 2, 3, 4, 5]
##
##**28 Find the longest word in the sentence**
##
##**29 write a program to reverse the values in the dictionary if the value is of type String**
##>>> d = {'a': 'hello', 'b': 100, 'c': 10.1, 'd': 'world'}
##
##**30 write a program to get 1234
##t = ('1', '2', '3', '4')
##
##**31 How to get the elements that are in list b but not in list a**
##a = [1, 2, 3] 
##b = [1, 2, 3, 4]
##
##**32 A function takes variable number of positional arguments as input. How to check if the arguments that are passed are more than 5**
##
##**33 Count the number of occurrences of "CRITICAL", "INFO" and "ERROR" lines in a log file.**
##```python
### Assume Below is the contents of the log file
##
##lines = """CRITICAL:Hello world
##INFO: This is an info
##ERROR: This is an error 
##CRITICAL: This is critical
##CRITICAL:Hello world
##INFO: This is an info
##ERROR: This is an error 
##CRITICAL: This is critical
##CRITICAL:Hello world
##INFO: This is an info
##ERROR: This is an error 
##CRITICAL: This is critical
##CRITICAL:Hello world
##INFO: This is an info
##ERROR: This is an error 
##CRITICAL: This is critical"""
##
##**34 Write a function to reverse any iterable without using reverse function.
##
##**35 Write a function to print the below output.**
##
### func("TRACXN", 0)  # Should print RCN
### func("TRACXN", 1)  # Should print TAX
##
##**36 Sum all the numbers in the below string.**
##s = "Sony12India567Pvt2ltd"
##
##**37 Write a program to sum all the numbers in below string.**
##s = "Sony12India567Pvt2ltd" # eg.12+567+2
##
##**38 Print all the numbers in the below list**
##a = ['abc', '123', 'hello', '23']
##
##**39 Program to print the number of occurrences of characters in a String without using inbuilt functions.**
##
##**40 Program to print only the repeated characters and count of the same.**
