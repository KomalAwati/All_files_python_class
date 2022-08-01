#  write a program to merge two list ?
l1 = [1, 2, 3]
l2 = [4, 5, 6]

# 1
print(l1 + l2)  #   [1, 2, 3, 4, 5, 6]

# 2
l3 = [*l1, *l2]
print(l3)   #       [1, 2, 3, 4, 5, 6]

# using chain()
from itertools import chain
res = chain(l1, l2)
print(res)   #   <itertools.chain object at 0x0000008E7E99AE30>
print(list(res))  #   [1, 2, 3, 4, 5, 6]

