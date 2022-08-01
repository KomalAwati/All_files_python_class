# 1. Building a dict of word and length pair

words = "This is a bunch of words"
d = {}
for word in words.split():
    if word not in d:
        d[word] = len(word)
    
print(d)

# {'This': 4, 'is': 2, 'a': 1, 'bunch': 5,
#  'of': 2, 'words': 5}
