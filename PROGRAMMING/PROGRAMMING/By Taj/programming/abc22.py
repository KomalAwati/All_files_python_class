sentence = 'python is a good programming language'
words = sentence.split()

d = { word: len(word)    for word in words }

print(d)  #  {'python': 6, 'is': 2, 'a': 1, 'good': 4, 'programming': 11, 'language': 8}

largest_word = sorted(d.items(), key= lambda item: item[-1])

print(largest_word)    #  [('a', 1), ('is', 2), ('good', 4), ('python', 6), ('language', 8), ('programming', 11)]

print(largest_word[-1])   #   ('programming', 11)

