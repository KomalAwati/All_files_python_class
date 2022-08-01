'''
s = "Hello WOrld"
def convert():
    return list(s)
def convert_list(list_):
    return "".join(list_)
'''
#******************************************************************
#Pgm - 4th
'''
s1 = s.split(",")

s1.replace(" " , ",")
print(s1)

#Using Join And split
s1 = s.split()
'''
#Replace a string with another
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
            

#******************************************************************

s = 'Hello world welcome to python'
'''
print(s.replace(" ",','))
'''

#O/p-
#Hello,world,welcome,to,python

#split-join
'''
words = s.split()
print(','.join(words))
'''
#O/p-
#Hello,world,welcome,to,python

#list()
'''
chars = list(s)
print(','.join(chars))
'''
#O/p-
#H,e,l,l,o, ,w,o,r,l,d, ,w,e,l,c,o,m,e, ,t,o, ,p,y,t,h,o,n

#******************************************************************
#CSV to List
#A CSV( Comma Separated Values) string, as its name suggests is a string consisting of values or data separated by commas.
#given string
string1="abc,def,ghi"
print("Actual CSV String: ",string1)
print("Type of string: ",type(string1))
 
#spliting string1 into list with ',' as the parameter
print("CSV coverted to list :",string1.split(','))
#O/p-
#Actual CSV String:  abc,def,ghi
#Type of string:  <class 'str'>
#CSV coverted to list : ['abc', 'def', 'ghi']




































'''
s = "Hello WOrld"
l = list(s)
print(l)

#o/p- 
['H', 'e', 'l', 'l', 'o', ' ', 'W', 'O', 'r', 'l', 'd']
'''
