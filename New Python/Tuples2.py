t = ('a','b','c','d')

a = t[2]

print(a) #2

#Updating tuple
t = ('a','b','c','d')

s = list(t)

s[2] = 'f'

t = tuple(s)

print(t) #('a', 'b', 'f', 'd')


#adding item
t = ('a','b','c','d')

s = list(t)

s.append('f')

t = tuple(s)

print(t) # ('a', 'b', 'c', 'd', 'f')

#adding item

t = ('a','b','c','d')

s = (1,2,3)

res = t + s

print(res) #('a', 'b', 'c', 'd', 1, 2, 3)

#remove item
t = ('a','b','c','d')

s = list(t)

s.remove('b')

t = tuple(s)

print(t) #('a', 'c', 'd')

#delete the tuple
t = ('a','b','c','d')

del t

#print(t) #NameError: name 't' is not defined

#Packing

t = ('a','b','c','d')

print(t)

fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(fruits) #('apple', 'banana', 'cherry')



fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

alpha = ('a','b','c','d')

(aaa, bbb,*ccc) = alpha

print(aaa)
print(bbb)
print(ccc)


#a
#b
#['c', 'd']

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

'''a = (1,2,3,4,"aa", "a+3j")
for x in a:
    print(x)

Loop Through the Index Numbers'''
