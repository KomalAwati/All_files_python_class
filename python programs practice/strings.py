'''
#Join
data = 'Hie'

print(data.join(['hello', 'world']))

#helloHieworld

#***********************************************************************************************************
message = 'hello'
print('_'.join(message))

#h_e_l_l_o

#***********************************************************************************************************
message1 = 'Hello baby'
print('*'.join(message1))

#H*e*l*l*o* *b*a*b*y

#***********************************************************************************************************
#strip()
print('this is my string'.split('s'))


#['thi', ' i', ' my ', 'tring']


#***********************************************************************************************************

message = 'hello world'

print(message.index('l')) #2

print(message.rindex("l")) #9

#print(message.index('Hello')) #ValueError

#***********************************************************************************************************
fruits = ["apple", "banana", "cherry"]

x = fruits.count("cherrry")

print(x)
#***********************************************************************************************************
txt = "Hello, welcome to my world."

x = txt.rfind("world") #21

print(x) #7

#***********************************************************************************************************
list = [1,2,3,4,5,2,3,]

print(list.index(2)) #1

#***********************************************************************************************************
#Converting the string to list and vice versa

s = 'Hello'
print(s.split()) #['Hello']
#list= list(1)
#print(list)
#***********************************************************************************************************
'''
my_list = list('helloworld')
print(my_list) #['h', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd']

print(''.join(['h', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd']))
#helloworld
print(' '.join(['h', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd']))
#h e l l o w o r l d
name = 'Komal'
print(list(name)) #['K', 'o', 'm', 'a', 'l']

#***************************************************************************************
#deepcopy() -


# importing copy module
import copy
  
# initializing list 1 
li1 = [1, 2, [3,5], 4]
  
  
# using copy for shallow copy  
li2 = copy.copy(li1)
print(li2)
  
# using deepcopy for deepcopy  
li3 = copy.deepcopy(li1)
print(li3)
