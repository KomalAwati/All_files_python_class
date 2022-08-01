sentence = "python is a good programming language and programming is fun"
words = sentence.split()
longest = ""
for word in words:
    if len(longest) < len(word): #  if len(longest) < len(word) and words.count(word) == 1:
        if words.count(word) == 1:
            longest = word

print(longest)
