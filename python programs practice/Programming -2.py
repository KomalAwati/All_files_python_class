#*********************************************************************************
#Program -1st
#isinstance('hello', str)
'''
def check_string(string):
    if isinstance(string, str):
        return True
    return False

d = check_string('hello')
print(d)
'''
#O/p-
#True
#Or
'''
def check_string(string):
    return isinstance(string, str)
d = check_string('hello')
print(d)
'''
#O/p-
#True

#*********************************************************************************
#Program -2nd
#Write a Python program to swap cases of a given string.

#inbuilt methods by mam -
'''
def swap(char):
    if char.islower():
        return char.upper()
    if char.isupper():
        return char.lower()
print(swap('A'))
'''
#O/p - a

#*********************************************************************************
#Without using inbuilt methods by mam -
'''
def swap_case(char):
        if ord('a') <= ord(char) <= ord('z'): #if ord(char) >= ord('a') and ord(char) <= ord('z'):
            print(chr(ord(char)-32))
            
        elif ord('A') <= ord(char) <=ord('z'):
            print(chr(ord(char) + 32))
'''
#O/p-
#swap_case('D')
#d
            
        

'''
ord(char)
100
ord("p")
60

prd(char) > 32
60
char(60)
'p'
char(ord(char) -32)
"p"
char(ord)
'''            
    

'''
def swap_case_string(str1):
   result_str = ""   
   for item in str1:
       if item.isupper():
           result_str += item.lower()
       else:
           result_str += item.upper()           
   return result_str
print(swap_case_string("Python Exercises"))
'''

#*********************************************************************************
'''
string="my NaME is VaMsi"
lis=string.swapcase().split(" ")
print(lis)
'''
#O/p-
#['MY', 'nAme', 'IS', 'vAmSI']
#*********************************************************************************
#*********************************************************************************
#Program -3rd 
'''
def palindrome(string):
    res = ""

    for char in string:
        res = char + res
    if res == string:
        return f"{string} is palindrome"
    return f"{string} is palindrome"
'''

#O/p-
#palindrome('mom')
#'mom is palindrome'

#*********************************************************************************
#*********************************************************************************
#Program -4th 
string = 'The quick brown fox jusmps over the lazy dog'
# Define your variables
'''
def replace(string):
    res = ""
    for char in string:
        if char.lower() in "aeiou":
            res += "*"
        else:
            res += char
    return res
'''

#O/p -
#replace('komal')
#'k*m*l'

#*********************************************************************************
                                        #OR
'''
result = ''
for i in string:
        if i == 'o':
                i = '0'
        result += i
print result
'''

#*********************************************************************************
#Program - 5th
'''
def rep_char(string):
    res = ""
    for char in string:
        if string.count(char) > 1:
            res += "-"
        else:
            res += char
print(rep_char("KomalKom"))
'''
#O/p-
#None
            



