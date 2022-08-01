

sentence = "hello world welcome to python"
d = {}
for char in sentence:
    if char not in d and char == ' ':
        d[char] = sentence.count(char)

print(d)   #   {' ': 4}
