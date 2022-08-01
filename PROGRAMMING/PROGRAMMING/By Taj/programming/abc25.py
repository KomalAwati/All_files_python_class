sentence = "hello"
d = {}
for char in sentence:
    if char not in d and sentence.count(char) > 1:
        d[char] = sentence.count(char)

# print(d)  #    {'h': 2, 'e': 3, 'l': 4, 'o': 5, ' ': 4, 'w': 2, 't': 2}

# sort_d = sorted(d.items(), key= lambda item: item[-1])

# print(sort_d)   #   [('h', 2), ('w', 2), ('t', 2), ('e', 3), ('l', 4), (' ', 4), ('o', 5)]

from collections import defaultdict
dd = defaultdict(int)
for char in sentence:
    dd[char] += 1

print(dd)
