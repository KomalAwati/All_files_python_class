
'''x = "malayalam"
 
w = ""
for i in x:
    w = i + w
 
if (x == w):
    print("Yes")
else:
    print("No")'''

#*************************************************************
'''
user_string = input()
sub = "too good"
rep_sub = "excellent"
low = user_string.find(sub)
high = low + len(sub)
if sub in user_string:
    replaced_string = user_string[:low] + rep_sub + user_string[high:]
    print(replaced_string)
else:
    print(user_string)
    '''
#*************************************************************
                                                        #Create a string made of the first, middle and last character
#Write a program to create a new string made of an input string’s first, middle, and last character.
#str1 = "James"
#Expected Output: Jms
'''str1 = 'James'
print("Original String is", str1)

res = str1[0]

l = len(str1)

mi = (l/2)

res = res + str1[mi]

res = res +str1[l-1]

print("New string :", res)'''

#*************************************************************
'''
str1 = "Komal"
print("Original String is" , str1)
res = str1[0]

l = len(str1)

mi = int(l/2)

res = res + str1[mi]

res = res + str1[l-1]

print("String After the concatenation :", res)
'''
#O/p -
#Original String is Komal
#String After the concatenation : Kml
#*************************************************************
'''
name = "Qomal"

print("Original String ", name)

res = name[0]

l = len(name)

mi = int(l/2)

res = res + name[mi]

res = res + name[l-1]

print("New String :" , res)

#O/p-
#Original String  Qomal
#New String : Qml
'''

#*************************************************************
                                                                #Create a string made of the middle three characters
#str1 = "JhonDipPeta"
#O/p - Dip
#str2 = "JaSonAy"
#O/p - Son
'''
def get_middle_three_chars(str1):
    print("old", str1)
    l = len(str1)
    mi = int(l/2)
    res = str1[mi-1:mi + 2]
    print("Middle 3 chars are : ", res)
    
get_middle_three_chars('JhonDipPeta')
get_middle_three_chars("JaSonAy")
'''

#*************************************************************
'''
def mid(a):
    mi = int(len(a)/2)
    res = a[mi-1:mi+2]
    print(res)

mid("PraBHAkar")
'''
#O/p - BHA


#*************************************************************
'''
def mid(a):
    mi = int(len(a)/2)
    res = a[mi-1:mi+2]
    print("Mid string", res)

mid("PraBHAkar")

#O/p - Mid string BHA
'''

#*************************************************************
                                                                #Append new string in the middle of a given string
#s1 = "Ault"
#s2 = "Kelly"

#Expected Output: AuKellylt

'''

def append_middle(s1, s2):
    print("Original Strings are", s1, s2)

    # middle index number of s1
    mi = int(len(s1) / 2)

    # get character from 0 to the middle index number from s1
    x = s1[:mi:]
    # concatenate s2 to it
    x = x + s2
    # append remaining character from s1
    x = x + s1[mi:]
    print("After appending new string in middle:", x)

append_middle("Ault", "Kelly")

'''

#O/p-
#Original Strings are Ault Kelly
#After appending new string in middle: AuKellylt





































