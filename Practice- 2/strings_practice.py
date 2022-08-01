# String Functions
# Python has a set of built-in methods that you can use on strings.
# NOTE: ALL STRING FUNCTIONS RETURNS A NEW STRING AND WILL NOT MODIFY OR MUTATE THE EXISTING STRING.
#**************************************************************************************************
#Function 1st - capitalize()
#Converts the first character to upper case
        #capitalize() - It capitalizes the first character of the String. This function is deprecated in python3
# Python capitalize() function example -1st 

#name = "komal" # Variable declaration
'''
# Calling function  
new_name = name.capitalize()  
# Displaying result  
print("Old value:", name)  
print("New value:", new_name)
'''
#O/p-
#Old value: komal
#New value: Komal

# Python capitalize() function example - 1st - Practice
'''
c_name = 'vtu'
new_c_name = c_name.capitalize()
print("Old name : " , c_name)
print("new name : ", new_c_name)
'''
#O/p-
#Old name :  vtu
#new name :  Vtu

#**************************************************************************************************
# Python capitalize() function example -2nd 
#It returns a version of s suitable for case-less comparisons.
#What if first character already exist in uppercase.
#name = "Komal" # Variable declaration
# Calling function  
#new_name = name.capitalize()  #It returns the same string without any alteration.
# Displaying result
'''
print("Old value:", name)  
print("New value:", new_name)
'''

#O/p-
#Old value: Komal
#New value: Komal


#**************************************************************************************************
# Python capitalize() function example -3rd
#What if first character is a digit or non-alphabet character? This method does not alter character if it is other than a string character.
'''
subject = "#python"
n_subject = subject.capitalization()
print("Old Value : " , subject)
print("Old Value : " , n_subject)
'''
#This method does not alter character if it is other than a string character.
#**************************************************************************************************
# Python capitalize() function example -3rd
# Python capitalize() function example  
# Variable declaration

'''
str = "#javatpoint"  
# Calling function  
str2 = str.capitalize()  
# Displaying result  
print("Old value:", str)  
print("New value:", str2)  
print("--------digit---------")  
str3 = "1-javatpoint"  
str4 = str3.capitalize()  
print("Old value:", str3)  
print("New value:", str4)

'''

#O/p -
#Old value: #javatpoint
#New value: #javatpoint
#--------digit---------
#Old value: 1-javatpoint
#New value: 1-javatpoint

#*****************************************************************************************************
#*****************************************************************************************************

                                                            #casefold()

#It returns a version of s suitable for case-less comparisons.
#Casefold() method returns a lowercase copy of the string.
#It is more simillar to lowercase method except it revomes all case distinctions present in the string.
#**************************************************************************************************
#Function 1st - casefold()
#str = "JAVATPOINT"  
# Calling function  
#str2 = str.casefold()  
# Displaying result  
#print("Old value:", str)  
#print("New value:", str2)

#O/p-
#Old value: JAVATPOINT
#New value: javatpoint

#**************************************************************************************************
#Function 2nd - casefold()
#str = "JAVATPOINT"  
# Calling function  
#str2 = str.casefold()  
# Displaying result  
#print("Old value:", str)  
#print("New value:", str2)


#*****************************************************************************************************
#*****************************************************************************************************
#String to list coversion
#1st Way - #Using Split
# Driver code
'''
str1 = "Geeks for Geeks"
print(str1.split())
'''

#*****************************************************************************************************
#*****************************************************************************************************
#Using Split
'''
str_1 = "Hire-the-top-1%-freelance-developers"

list_1 = str_1.split("-")
print(list_1)
'''
#O/p - 
['Hire', 'the', 'top', '1%', 'freelance', 'developers']

#*****************************************************************************************************
#*****************************************************************************************************
                                            #Python code to convert string to list character-wise
'''
def Convert(string):
    list1=[]
    list1[:0]=string
    return list1
# Driver code
str1="ABCD"
print(Convert(str1))
'''
#O/p
['A', 'B', 'C', 'D']

#*****************************************************************************************************
#*****************************************************************************************************

#2nd Way - #Using list(typecasting)
'''
str_1 = "Hire freelance developers"
list_1 = list(str_1.strip(" "))
print(list_1)
'''

#O/p
['H', 'i', 'r', 'e', ' ', 'f', 'r', 'e', 'e', 'l', 'a', 'n', 'c', 'e', ' ', 'd', 'e', 'v', 'e', 'l', 'o', 'p', 'e', 'r', 's']
#*****************************************************************************************************
#*****************************************************************************************************
                                             # Python program to convert a list to string
#There are 4 ways:
#1 - Iterate through the list
#2 - Using join() function
#3 - Using list comprehension
#4 - Using map()

#*****************************************************************************************************                                             
#1st Way -
# Iterate through the list and keep adding the element for every index in some empty string.
'''
def listToString(s): 
    
    # initialize an empty string
    str1 = "" 
    
    # traverse in the string  
    for ele in s: 
        str1 += ele  
    
    # return string  
    return str1 
        
        
# Driver code    
s = ['Geeks', 'for', 'Geeks']
print(listToString(s))
'''

#O/p-
#GeeksforGeeks

#*****************************************************************************************************
#2nd Way
# Python program to convert a list
# to string using join() function
    
# Function to convert
'''
def listToString(s): 
    
    # initialize an empty string
    str1 = " " 
    
    # return string  
    return (str1.join(s))
        
        
# Driver code    
s = ['Geeks', 'for', 'Geeks']
print(listToString(s))
'''
#O/p-
#Geeks for Geeks
#*****************************************************************************************************

# Python program to convert a list
# to string using list comprehension
''' 
s = ['I', 'want', 4, 'apples', 'and', 18, 'bananas']
  
# using list comprehension
listToStr = ' '.join([str(elem) for elem in s])
  
print(listToStr)
'''
#O/p-
#I want 4 apples and 18 bananas

#*****************************************************************************************************
# Python program to convert a list
# to string using list comprehension
'''  
s = ['I', 'want', 4, 'apples', 'and', 18, 'bananas']
  
# using list comprehension
listToStr = ' '.join(map(str, s))
  
print(listToStr)
'''
#O/p
#I want 4 apples and 18 bananas
#*****************************************************************************************************
#*****************************************************************************************************
                                                #How To Convert Python String To Dictionary
#1 - Using inbuilt method count
#2 - Not using inbuilt method

'''
string = 'Hello World'
d={}
for char in string:
    d[char] = string.count(char)
print(d)
'''
#O/p
#{'H': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'W': 1, 'r': 1, 'd': 1}

#*****************************************************************************************************

#2 - Using split, for and if
'''
text = "hello there hi there"
dic = dict()
for w in text.split():
    if w in dic.keys():
        dic[w] = dic[w]+1
    else:
        dic[w] = 1
print(dic)
'''
#O/p
#{'hello': 1, 'there': 2, 'hi': 1}

#*****************************************************************************************************
# Python implementation of converting
# a string into  a dictionary
 
# initialising first string
str1 = "Jan, Feb, March"
str2 = "January | February | March"
 
# splitting first string
# in order to get keys
keys = str1.split(", ")
 
# splitting second string
# in order to get values
values = str2.split("|")
 
# declaring the dictionary
dictionary = {}
 
# Merging all keys and values
# to generate items for
# the dictionary
dictionary = dict(zip(keys, values))
 
# printing the generated dictionary
print(dictionary)

#O/p
#{'Jan': 'January ', 'Feb': ' February ', 'March': ' March'}

#*****************************************************************************************************
                                                                #DefaultDict
#Defaultdict is a container like dictionaries present in the module collections.
#Defaultdict is a sub-class of the dictionary class that returns a dictionary-like object.
#The functionality of both dictionaries and defaultdict are almost same except for the fact that defaultdict never raises a KeyError. It provides a default value for the key that does not exists.
#Syntax: defaultdict(default_factory)
#Parameters:  
#default_factory: A function returning the default value for the dictionary defined.
#If this argument is absent then the dictionary raises a KeyErro


# Python program to demonstrate
# defaultdict
  
  
#from collections import defaultdict
  
  
# Function to return a default
# values for keys that is not
# present
'''
def def_value():
    return "Not Present"
      
# Defining the dict
d = defaultdict(def_value)
d["a"] = 1
d["b"] = 2
  
print(d["a"])
print(d["b"])
print(d["c"])
'''
#O/p-
#{'Jan': 'January ', 'Feb': ' February ', 'March': ' March'}
#1
#2
#Not Present
