#  wap to create a dict of first char and the word starting with that first char pair

from collections import defaultdict

sentence = "my name is mohammad taj hassan and python is a good programming language"

words = sentence.split()
d={}
for word in words:
    if word[0] not in d:
        d[word[0]] = [word]
    else:
        d[word[0]] +=  [word]

print(d)

# output:-  {'m': ['my', 'mohammad'], 'n': ['name'], 'i': ['is', 'is'], 't': ['taj'], 
#             'h': ['hassan'], 'a': ['and', 'a'], 'p': ['python', 'programming'], 
#              'g': ['good'], 'l': ['language']}

dd = defaultdict(list)
words = sentence.split()
for word in words:
    dd[word[0]].append(word)

print(dd)

#  output:-  defaultdict(<class 'list'>, {'m': ['my', 'mohammad'], 'n': ['name'], 
#               'i': ['is', 'is'], 't': ['taj'], 'h': ['hassan'], 'a': ['and', 'a'], 
#               'p': ['python', 'programming'], 'g': ['good'], 'l': ['language']})