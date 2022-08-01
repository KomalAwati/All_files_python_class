# WAP to get below output ?

sentence = "hello world welcome to python programming hi there"

d = {}
for word in sentence.split():
    if word[0] not in d:
        d[word[0]] = [word]
    else:
        d[word[0]].append(word)
print(d)

#output:-   {'h': ['hello', 'hi'], 'w': ['world', 'welcome'], 't': ['to', 'there'], 'p': ['python', 'programming']}

#  2
from collections import defaultdict
dd = defaultdict(list)
for word in sentence.split():
    dd[word[0]].append(word)  #  dd[word[0]] += [word]

print(dd)

#output:-  defaultdict(<class 'list'>, {'h': ['hello', 'hi'], 'w': ['world', 'welcome'], 't':
#                ['to', 'there'], 'p': ['python', 'programming']})



