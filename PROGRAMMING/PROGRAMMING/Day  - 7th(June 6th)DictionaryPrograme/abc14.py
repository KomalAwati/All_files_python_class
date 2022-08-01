#  dict comprenhension

words = "This is bunch of words"
l = words.split()
d = { word: len(word)  for word in l}

print(d)

# {'This': 4, 'is': 2, 'bunch': 5, 'of': 2, 'words': 5}
