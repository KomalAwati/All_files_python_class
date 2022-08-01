#*********************************************************************************************************
#*********************************************************************************************************
#Program - 1st
#To find the len of iterable without using any inbuilt function
'''
string = 'Hello'
count = 0
for _ in string:
    count+=1
print(count)
'''
#O/p
#5

string = 'Komal'
count = 0
for _ in string:
    count += 1
print(count)

#*********************************************************************************************************
#Program - 2nd
#WAP reverse a string without using any inbuilt method
#Using range:
'''
string = 'Hello'
rev_str = string[::-1] or #rev_str = string[-1:-len(string)-1:-1
print(rev_str)
'''
#O/p -
#olleH


#*********************************************************************************************************
                                                    #or
#By Net - By using for loop
'''
my_string=("Nitesh Jhawar")
str=""
for i in my_string:
    str=i+str
print("Reversed string:",str)
or
'''
#O/p-
#Reversed string: rawahJ hsetiN

#or - By Mam
'''
my_string=("Hello")
str=""
for char in my_string:
    str = char + str
print("Reversed string:",str)
'''
#O/p-
#Reversed string: olleH


#*********************************************************************************************************
#*********************************************************************************************************
#Program - 2nd
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

#*********************************************************************************************************

#method -2nd - With using inbuilt function
#s = 'hello world'
#print(s.replace("world", "universe")) 

#O/p - 
#hello universe

#*********************************************************************************************************
#*********************************************************************************************************
#WAP to convert string into list and vice versa
#Program - 3rd
#Method - 1st #Using Split()
'''
str_1 = "Hire the top 1% freelance developers"
list_1 = str_1.split()
print(list_1)
'''

#Output:
#['Hire', 'the', 'top', '1%', 'freelance', 'developers']

#*********************************************************************************************************
#or
'''
str_1 = "Hire freelance developers"
list_1 = list(str_1.strip(" "))
print(list_1)
'''

#Output:
#['H', 'i', 'r', 'e', ' ', 'f', 'r', 'e', 'e', 'l', 'a', 'n', 'c', 'e', ' ', 'd', 'e', 'v', 'e', 'l', 'o', 'p', 'e', 'r', 's']

#*********************************************************************************************************

#Method - 2nd #Typecasting
'''
#given string
string1="AskPython"
 
#printing the string
print("Actual String: ",string1)
#confirming the type()
print("Type of string: ",type(string1))
 
#type-casting the string into list using list()
print("String coverted to list :\n",list(string1))
'''

#Output
#Actual String:  AskPython
#Type of string:  <class 'str'>
#String coverted to list :
# ['A', 's', 'k', 'P', 'y', 't', 'h', 'o', 'n']

#*********************************************************************************************************
#Method - 3rd #By using map
#Given string
'''
string1="This is Python"
 
print("The actual string:",string1)
 
#converting string1 into a list of strings
string1=string1.split()
 
#applying list method to the individual elements of the list string1
list1=list(map(list,string1))
 
#printing the resultant list of lists
print("Converted to list of character list :\n",list1)
'''
#Output - 
#The actual string: This is Python
#Converted to list of character list :
#[['T', 'h', 'i', 's'], ['i', 's'], ['P', 'y', 't', 'h', 'o', 'n']]

#*********************************************************************************************************
#given string
'''
string1="abc,def,ghi"
print("Actual CSV String: ",string1)
print("Type of string: ",type(string1))
 
#spliting string1 into list with ',' as the parameter
print("CSV coverted to list :",string1.split(','))
'''
#*********************************************************************************************************
#A string consisting of Integers to List of integers
#string with integers sepated by spaces

string1="1 2 3 4 5 6 7 8"
print("Actual String containing integers: ",string1)
print("Type of string: ",type(string1))
 
#coverting the string into list of strings
list1=list(string1.split())
print("Converted string to list : ",list1)
 
#typecasting the individual elements of the string list into integer using the map() method
list2=list(map(int,list1))
print("List of integers : ",list2)

#O/p -

#Actual String containing integers:  1 2 3 4 5 6 7 8
#Type of string:  <class 'str'>
#Converted string to list :  ['1', '2', '3', '4', '5', '6', '7', '8']
#List of integers :  [1, 2, 3, 4, 5, 6, 7, 8]
#********************************************************************************************************
#CSV to List
#A CSV( Comma Separated Values) string, as its name suggests is a string consisting of values or data separated by commas.
'''
#given string
string1="abc,def,ghi"
print("Actual CSV String: ",string1)
print("Type of string: ",type(string1))
 
#spliting string1 into list with ',' as the parameter
print("CSV coverted to list :",string1.split(','))
'''
#O/p-
#Actual CSV String:  abc,def,ghi
#Type of string:  <class 'str'>
#CSV coverted to list : ['abc', 'def', 'ghi']

#*********************************************************************************************************
#Program - 4th
#WAP to convert string into comma separated value
'''
s = 'Hello world welcome to python'
print(s.replace(" ",','))
'''

#O/p - 
#Hello,world,welcome,to,python






