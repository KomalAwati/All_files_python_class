#Program - 1st
# WAP to merge a two lists
'''
l1 = [1,2,3]
l2 = [4,5,6]

print(l1 + l2)

l3 =[*l1, *l2]
'''

#o/p-
#[1, 2, 3, 4, 5, 6]

#*******************************************************************************************
#Program - 2nd

#chain - modules itertools
#concatenate using iterables (+ means add it to last)

#merge any no. of iterables we make a use of "chain"

#wnvr uh using arithmetic operator it shoud be has same data type

#Chainmap - all the 

#from itertools import chain
#res = chain(11,12)


#o/p-
#res

#list(res)

#*******************************************************************************************
#Program - 2nd
#Write a pgm to get the elements that are in the list b but not in the list a
'''
A=[1,2,3,4]
B=[4,5,6,7]

>>> 3 not in [2, 3, 4]
False
>>> 3 not in [4, 5, 6]
True
'''

#*******************************************************************************************
'''
A=[1,2,3,4]
B=[4,5,6,7]

>>> 3 not in [2, 3, 4]
False
>>> 3 not in [4, 5, 6]
True
'''

#*******************************************************************************************
#terminal
'''
set(a).difference(set(b))
set()
set(b).difference(set(a))
[4]
set(b) - set(a)
[4]
difference - new set
difference
'''

#*******************************************************************************************
'''
a=[1,2,3,4]
b=[4,5,6,7]
for item in b:
    if item not in a:
        print(item, end = " ")
'''

#*******************************************************************************************

#Program - 3rd
#wap to build the list having even#WAP to build a list with only the items having even no. of items
'''
names = ['a','b','c','d']

res = [name for name in names if len(name) % 2 == 0]
'''
#*******************************************************************************************
#Program - 4th
#reverse a each word of the string
#string = "hello Komal how are you"
#o/p-
'''
for word in string.split():
    print(word[::-1], end = " ")
'''
#O/p-
#olleh lamoK woh era uoy 

#*******************************************************************************************
#Program - 5th
#WAP to check wheather given no is Prime or not.
'''
num = 5
for i in range(2, num):
    if num % i == 0:
        print('this no. is not a prime')
        break
    else:
        print("no. is prime")
'''

#*******************************************************************************************
'''   
    num = 5
for i in range(2, num):
    if num % i == 0:
        print('this no. is not a prime')
        break
    else:
print("no. is prime")
'''
#*******************************************************************************************
                                            # Correct Pgm
'''
num = 2
for i in range(2, num):
    if num % i == 0:
        print('this no. is not a prime')
        break
else:
    print("no. is prime")
'''

#O/p-
#no. is prime

#*******************************************************************************************
'''
num = 2
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print('this no. is not a prime')
            break
            
    
        
else:
    print("no. is prime")
'''

#*******************************************************************************************
'''
num = 9
for num in range(1,10):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)
            '''
        
#O/p-
'''    
2
3
5
7
'''


#*******************************************************************************************
#create a list comprehension to check whethr no. is prime or not
#Using list comprehension
#[x for x in range(2, 20) if all(x % y != 0 for y in range(2, x))]

#Note
#we cannot use the control statement - pass,break , continue
#you cannot use assignment operators

#any - inbuilt function
'''

both take iterables as i/p
check for any one valuewhich is not empty

true - any one is true


any ([1,2,3])
True
'''
#all

#all

#all d elemnts are false and one is true - False

#all the elements should true - true

#*******************************************************************************************
'''
l = []
num = 8
for i in range(2, num):
    if num % i == 0:
        l.append(False)
    else:
        l.append(True)

res = [num % i for i in range(2, num)]

#O/p-
l

all(l)
False

'''

#*******************************************************************************************

l = []
num = 8
for i in range(2, num):
    if num % i == 0:
        l.append(False)
    else:
        l.append(True)


res = []
for i in range(2,num):
    res.append(num % i)

#*******************************************************************************************
'''    
num = 5
res = [num % i for i in range(2, num)]
print(all(res))
'''

#O/p-
#True


#O/p-
#res

#all(res)
    
