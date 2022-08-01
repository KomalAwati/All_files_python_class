#Packing the tuple
t = (1,2,4,5) #Packing
print(t)

a, b, c, d = t # Unpacking
print(d)

#Modifying the tuple
#Since tuples are immutable we cannot modify them directly instead of that we can modify them indirectly
#there are 2 ways
#1. Using unpacking of the tuple
#2. Using list() and tuple()

#1. Using unpacking of the tuple

t = (1,2,4,5) #Packing
print(t)

a, b, c, d = t # Unpacking
print(d)

a = 6
t = (a,b, c, d)
print(t) #(6, 2, 4, 5)

#2. Using list() and tuple()
t1 = (2,3,4,5)
l = list(t)
print(l)

l[2] = 6
print(l)

t1 =tuple(l)
print(t1)

