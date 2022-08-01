sentence = "python is a good programming language and programming is fun"

words = sentence.split()

d = { word: len(word)  for word in words if words.count(word) == 1}

print(d)   #  {'python': 6, 'a': 1, 'good': 4, 'language': 8, 'and': 3, 'fun': 3}

largest_repeat_word = sorted(d.items(), key= lambda item: item[-1] )

print(largest_repeat_word)  # [('a', 1), ('and', 3), ('fun', 3), ('good', 4), ('python', 6), ('language', 8)]

print(largest_repeat_word[-1])   #   ('language', 8)
