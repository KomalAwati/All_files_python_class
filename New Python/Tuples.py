#Creating the tuple
t = (1, )
print(t)

thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

t1 = (1,)
print(t)

t2 = (1)
print(t2)

tuple1 = ("abc", 34, True, 40, "male")
print(tuple1)

mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

#Creating the tuple using tuple constructor
tt1 = tuple((11,22,33)) #while the tuple construction we should give 2 parathesis
print(tt1)

#Access Tuple Items
thistuple = ("apple", "banana", "cherry")
print(thistuple[1]) #banana

th1 = (1,2,3,4)
print(th1[1]) #2

print(th1[-2]) #3


#Range of Indexes
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

thistuple1 = ('a','b','c','d')
print(thistuple1[:2])

#Range of Negative Indexes
print(thistuple1[-1:-3]) #()

thistuple2 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple2[-4:-1]) #('orange', 'kiwi', 'melon')

#Check if Item Exists
thistuple3 = ("apple", "banana", "cherry")
if "apple" in thistuple3:
  print("Yes, 'apple' is in the fruits tuple")

#('orange', 'kiwi', 'melon')
#Yes, 'apple' is in the fruits tuple

#Python - Update Tuples
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x) #('apple', 'kiwi', 'cherry')

a = ("Hi", "komal", "how", "are", "you")
b = list(a)
b[1]='baby'
a=tuple(b)
print(a) #('Hi', 'baby', 'how', 'are', 'you')

#Add Items
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)

#Add Items
ths = (1,2,3,4,5)
new_ths= list(ths)
new_ths.append(6)
ths = tuple(new_ths)
print(ths)

#add item 
#Using list typecasting
ttt = ('a','b','c','d')
ttt1 = list(ttt)
ttt1.append('e')
ttt = tuple(ttt1)
print(ttt) #('a', 'b', 'c', 'd', 'e')

#add item
#Using concatinations

ttt2 = ('a','b','c','d')
sss = ('e',)  

#or 

#sss = ('e') # it will give you the type error we cannot concatinate tuple with string
 
ttt2 = ttt2 + sss
print(ttt2) #('a', 'b', 'c', 'd', 'e')


#Remove Items
#Using list typecasting and remove()
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple) #('banana', 'cherry')


thist = ()




#The del keyword can delete the tuple completely:

thistuple111 = ("apple", "banana", "cherry")
del thistuple111
#print(thistuple111) #this will raise an error because the tuple no longer exists

#Unpacking
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

'''apple
banana
['cherry', 'strawberry', 'raspberry']'''

#Loop Through the Index Numbers
#Use the range() and len() functions to create a suitable iterable.
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
for i in range(len(fruits)):
  print(fruits[i])

'''apple
banana
cherry
strawberry
raspberry'''

alpha = ('a','b','c','d')

for i in range(len(alpha)):
  print(alpha[i])

'''
a
b
c
d
'''
#OR



alpha = ('a','b','c','d')

for i in range(4):
  print(alpha[i])

'''
a
b
c
d
'''  

#Using a While Loop

thistuple = ("apple", "banana", "cherry", 4)
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1

alpha = ('a', 'b', 'c', 1, 2,'d')

i = 0

while i < len(alpha):
  print(alpha[i])
  i = i + 1

'''
a
b
c
1
2
d'''

alpha = ('a', 'b', 'c', 1, 2,'d')

res = alpha * 3

print(res)

#('a', 'b', 'c', 1, 2, 'd', 'a', 'b', 'c', 1, 2, 'd', 'a', 'b', 'c', 1, 2, 'd')

thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.count(5)

y = thistuple.index(8)

print(x)

print(y)

thisset = {"apple", "banana", "cherry","apple", "banana", "cherry"}

print(len(thisset))

#Important questions
t = ('a', ) #('a',)
t = ('a','z', ) #('a', 'z')
print(t)

t1 = (1,2,3,4)
t2 = (5,6,7,8)

c = (*t1, *t2)
print(c)

#(1, 2, 3, 4, 5, 6, 7, 8)

t = (1,2,3,4,['Hai','Hello',23], 'python')
#x = t[4:0:-1] #(['Hai', 'Hello', 23], 4, 3, 2)
#x = t[4:1:-1] #(['Hai', 'Hello', 23], 4, 3)
x = t[3:3:-1] #(4,)
x = t[3:3:-1] #()
 
print(x) #TypeError: 'str' object does not support item assignment

a = [1,2,3]
b = [4,5,6]
print([a,b]) #[[1, 2, 3], [4, 5, 6]]


print((a,b)) #([1, 2, 3], [4, 5, 6])

