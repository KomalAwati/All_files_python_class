#  wap to create a dict of char and its index pair
'''
string = 'Malayalam'
d = {}
for index, char in enumerate(string):
    if char not in d:
        d[char]= [index]
    else:
        d[char]= d[char] + [index]
print(d)
'''

#O/p -
#{'M': [0], 'a': [1, 3, 5, 7], 'l': [2, 6], 'y': [4], 'm': [8]}

#Using defaultdict

'''
from collections import defaultdict
string = 'Malayalam'
dd = defaultdict(list)

for index, char in enumerate(string):
    dd[char] += [index]

print(dd)
'''
#O/p -
#defaultdict(<class 'list'>, {'M': [0], 'a': [1, 3, 5, 7], 'l': [2, 6], 'y': [4], 'm': [8]})
