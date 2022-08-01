

l1 = [2, 4, 3, 5, 6]
l2 = [0, 2, 4, 1]

def exponent(n1, n2):
    return n1 ** n2

power = lambda n1, n2: n1 ** n2
# print(power)            #   return address

print(list(map(exponent, l1, l2)))

#          or

print(list(map(power, l1, l2)))

# output [1, 16, 81, 5, 216]

from itertools import zip_longest
print(list(zip_longest(l1, l2)))

print(list(zip_longest(l1, l2, fillvalue= 100)))
