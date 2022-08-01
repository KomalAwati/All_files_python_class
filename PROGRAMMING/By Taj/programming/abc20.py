sentence = "python is a good programming language"
words = sentence.split()
d= {}
for word in words:
    d[word] = len(word)

print(d)   #    {'python': 6, 'is': 2, 'a': 1, 'good': 4, 'programming': 11, 'language': 8}

res = sorted(words, key = len)
# print(res)     #    ['a', 'is', 'good', 'python', 'language', 'programming']
sortest, *rest, longest = res
# print(sortest)
print(longest)

#  Normal program
longest = ""
for word in words:
    if len(word) > len(longest):
        longest = word  
print(longest)
