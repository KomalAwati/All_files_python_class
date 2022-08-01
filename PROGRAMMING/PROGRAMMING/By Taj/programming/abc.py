#  wap to create a dict of char and its index pair

string= "malayalam"
d={}
for index, char in enumerate(string):
    if char not in d:
        d[char] = [index]
    else:
        d[char] = d[char] + [index]

print(d)

#  output:- {'m': [0, 8], 'a': [1, 3, 5, 7], 'l': [2, 6], 'y': [4]}

from collections import defaultdict
dd=defaultdict(list)
for index, char in enumerate(string):
    dd[char] += [index]

print(dd)

# output:- defaultdict(<class 'list'>, {'m': [0, 8], 'a': [1, 3, 5, 7], 'l': [2, 6], 'y': [4]})