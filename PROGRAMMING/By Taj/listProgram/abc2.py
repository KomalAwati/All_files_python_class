#  WAP to get the elements that are in list b not in list a ?

a = [1, 2, 3, 4, 5]
b = [3, 4, 6, 7, 9]

#  1

d = set(b).difference(set(a))
print(d)   #    {9, 6, 7}

c = set(a).difference(set(b))
print(c)   #    {1, 2, 5}

#  2
for item in b:
    if item not in a:
        print(item, end=" ")

print()
