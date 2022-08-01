# Program - 1st
#https://www.geeksforgeeks.org/python-ways-to-sum-list-of-lists-and-return-sum-list/
# Python code to demonstrate
# sum of list of list
# using naive method
'''  
# Declaring initial list of list
L = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
          
# Printing list of list
print("Initial List - ", str(L))

# Using naive method
res = list()
for j in range(0, len(L[0])):
    tmp = 0
    for i in range(0, len(L)):
        tmp = tmp + L[i][j]
    res.append(tmp)
      
# printing result
print("final list - ", str(res))

#O/p- 
#Initial List -  [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#final list -  [12, 15, 18]

#*******************************************************************************************
                                                 # OR
# Python code to demonstrate
# sum of list of list using 
# zip and list comprehension
  
# Declaring initial list of list
List = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]
          
# Printing list of list
print("Initial List - ", str(List))
  
# Using list comprehension
res = [sum(i) for i in zip(*List)]
      
# printing result
print("final list - ", str(res))

#*******************************************************************************************
                                                    #OR
# using numpy array functions
# Python code to demonstrate
# sum of list of list
import numpy as np
  
# Declaring initial list of list
List = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])
          
# Printing list of list
print("Initial List - ", str(List))
  
# Using numpy sum
res = np.sum(List, 0)
      
# printing result
print("final list - ", str(res))

'''
#*******************************************************************************************
#*******************************************************************************************

# Program - 2nd
# Python program to print even Numbers in a List
'''
# list of numbers
list1 = [10, 21, 4, 45, 66, 93]
 
# using list comprehension
even_nos = [num for num in list1 if num % 2 == 0]
 
print("Even numbers in the list: ", even_nos)

#O/p-
#Even numbers in the list:  [10, 4, 66]
'''
#*******************************************************************************************
#*******************************************************************************************
'''
# Program - 3rd
# Python program to print
# duplicates from a list
# of integers
def Repeat(x):
    _size = len(x)
    repeated = []
    for i in range(_size):
        k = i + 1
        for j in range(k, _size):
            if x[i] == x[j] and x[i] not in repeated:
                repeated.append(x[i])
    return repeated
 
# Driver Code
list1 = [10, 20, 30, 20, 20, 30, 40,
         50, -20, 60, 60, -20, -20]
print (Repeat(list1))
     
#Output
#[20, 30, -20, 60]
'''
#*******************************************************************************************
#Method 2: Using Counter() function from collection module
'''
from collections import Counter
 
l1 = [1,2,1,2,3,4,5,1,1,2,5,6,7,8,9,9]
d = Counter(l1)
print(d)
 
new_list = list([item for item in d if d[item]>1])
print(new_list)

#O/p
Counter({1: 4, 2: 3, 5: 2, 9: 2, 3: 1, 4: 1, 6: 1, 7: 1, 8: 1})
#[1, 2, 5, 9]
'''
#*******************************************************************************************
#Method 3: Using count() method
# program to print duplicate numbers in a given list
# provided input
list = [1, 2, 1, 2, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 9]
 
new = []  # defining output list
 
# condition for reviewing every
# element of given input list
for a in list:
 
     # checking the occurrence of elements
    n = list.count(a)
 
    # if the occurrence is more than
    # one we add it to the output list
    if n > 1:
 
        if new.count(a) == 0:  # condition to check
 
            new.append(a)
 
print(new)
 
#Output
#[1, 2, 5, 9]
#*******************************************************************************************
#*******************************************************************************************
'''
#Program - 4th
#Method 1 (Simple approach)
#We keep a counter that keeps on increasing if the required element is found in the list.
def countX(lst, x):
    count = 0
    for ele in lst:
        if (ele == x):
            count = count + 1
    return count
 
# Driver Code
lst = [8, 6, 8, 10, 8, 20, 10, 8, 8]
x = 8
print('{} has occurred {} times'.format(x, countX(lst, x)))

#Output:
#8 has occurred 5 times
#*******************************************************************************************
                                                    #OR
#Method 2 (Using count())
# Python code to count the number of occurrences
def countX(lst, x):
    return lst.count(x)
 
# Driver Code
lst = [8, 6, 8, 10, 8, 20, 10, 8, 8]
x = 8
print('{} has occurred {} times'.format(x, countX(lst, x)))

#*******************************************************************************************
                                                    #OR
#(Using Counter()) 
#method returns a dictionary with occurrences of all elements as a key-value pair, where key is the element and value is the number of times that element has occurred.
from collections import Counter
 
# declaring the list
l = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
 
# driver program
x = 3
d = Counter(l)
print('{} has occurred {} times'.format(x, d[x]))

#O/p -
#3 has occurred 2 times

#*******************************************************************************************
#*******************************************************************************************
#Program 5th
# Python program to find the k most frequent words
# from data set
from collections import Counter
  
data_set = "Welcome to the world of Geeks " \
"This portal has been created to provide well written well" \
"thought and well explained solutions for selected questions " \
"If you like Geeks for Geeks and would like to contribute " \
"here is your chance You can write article and mail your article " \
" to contribute at geeksforgeeks org See your article appearing on " \
"the Geeks for Geeks main page and help thousands of other Geeks. " \
  
# split() returns list of all the words in the string
split_it = data_set.split()
  
# Pass the split_it list to instance of Counter class.
Counter = Counter(split_it)
  
# most_common() produces k frequently encountered
# input values and their respective counts.
most_occur = Counter.most_common(4)
  
print(most_occur)
'''