
sentence = "hello"
# using count()
d = {}
for char in set(sentence):
    d[char] = sentence.count(char)

print(d)   #    {'e': 3, 'w': 2, 'o': 5, 'l': 4, 'r': 1, 'd': 1,
           #      'h': 2, 't': 2, 'm': 1, 'y': 1, 'c': 1, ' ': 4, 'n': 1, 'p': 1}
for char in sentence:
    if char not in d:
        d[char] = 1
    else:
        d[char] = d[char] + 1

print(d) #  {'h': 2, 'e': 3, 'l': 4, 'o': 5, ' ': 4, 'w': 2, 'r': 1, 
          #     'd': 1, 'c': 1, 'm': 1, 't': 2, 'p': 1, 'y': 1, 'n': 1}

# from collections import defaultdict
# dd= defaultdict(int)
# for char in sentence:
#     dd[char] += 1

# print(dd)  #   defaultdict(<class 'int'>, {'h': 2, 'e': 3, 'l': 4, 'o': 5, ' ': 4, 'w': 2, 
           #           'r': 1, 'd': 1, 'c': 1, 'm': 1, 't': 2,'p': 1, 'y': 1, 'n': 1})
