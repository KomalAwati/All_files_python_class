'''point = (4, 5) # Unpacking Tuple
x, y = point
print(x)
print(y)'''
     
'''
data= ['Komal', 'Awati',1] # Unpacking list of items
name,sname,un= data
print(name)
print(sname)
print(un)
'''

'''
date =(24,5,2022)
y, m, d = date
print(y)
print(m)
print(d)
'''

'''
name='Komal'
a,b,c,d,e=name
print(a)
print(b)
print(c)
print(d)
print(e)
'''

'''
names = ['apple', 'google', 'gmail', 'yahoo', 'yahoo']

for item in enumerate(names):
    index,name=item
    print(index,name)

0 apple
1 google
2 gmail
3 yahoo
4 yahoo


for index, name in enumerate(names):
 print(index, name)
'''

'''
alphabates = ['a','b','c','d']
for char in enumerate(alphabates):
 index,name=char 
 print(index,name)

o/p-
0 a
1 b
2 c
3 d'''

'''
num=[1,2,3,4,5]
for number in enumerate(num):
 index,nums=number
 print(index,num)

o/p-

 0 [1, 2, 3, 4, 5]
1 [1, 2, 3, 4, 5]
2 [1, 2, 3, 4, 5]
3 [1, 2, 3, 4, 5]
4 [1, 2, 3, 4, 5]'''



# Tuple unpacking
#a = [1, 2, 3, 4]
#b = [5, 6, 7, 8]

# Tuple unpacking (unpcking in for loop)
'''
for item in zip(a,b):
 fst,snd = item
 print(fst, snd)

 o/p-
1 5
2 6
3 7
4 8
 '''

'''
for fst,snd in zip(a,b):
    print(fst)
    print(snd)

o/p-
1
5
2
6
3
7
4
8s

for fst,snd in zip(a,b):
    print(fst,snd)

o/p-
1 5
2 6
3 7
4 8
'''

# Unpacking a dictionary (method-1)
'''
d = {'one': 1, 'two':2, 'three': 3}
for item in d.items():
 k, v = item
 print(k, v)
'''

# Unpacking a dictionary (method-2)
'''
d1={"a":1,"b":2,'c':2}
for k,v in d1.items(): // We can get key and value pair with the help of items()
 print(k,v)

o/p-
a 1
b 2
c 2'''

# Normal unpacking
temperatures = {"Bangalore": (26, 32), "Chennai": (29, 35), "Delhi": (31, 36)}
'''for city, temperatures in temperatures.items():
 print(city, temperatures)

o/p-
Bangalore (26, 32)
Chennai (29, 35)
Delhi (31, 36)
'''


# Deep Unpacking
'''for city, (_min, _max) in temperatures.items():
 print(city, _min, _max)
o/p-
Bangalore 26 32
Chennai 29 35
Delhi 31 36'''



# Unpacking Elements from iterables of Arbitary length
# * is used to grab excess arguments/items
# * is called unpacking operator
'''
least, *rest, maximum = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(least) # Prints first item in the list #1
print(maximum) # Prints last item in the list #10
print(rest) # Prints all the item in between 1st and last item of the list #[2, 3, 4, 5, 6, 7, 8, 9]
print(max(rest)) #9
print(min(rest)) #2

'''

#trailing - Except the last attribute it will return the entire list
#current - 


*trailing, current = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(trailing) #[1, 2, 3, 4, 5, 6, 7, 8, 9]
#print(current) #10







