# 4. Counting the number of each character in a String

sentence = "hello world welcome to python hello hi world welcome to python"

d = {}
for char in sentence:
    if char not in d:
        d[char] = 1
    else:
        d[char] += 1

print(d)

# output:- {'h': 5, 'e': 6, 'l': 8, 'o': 10, ' ': 10, 'w': 4, 'r': 2, 'd': 2, 'c': 2, 'm': 2, 't': 4, 'p': 2, 'y': 2, 'n': 2, 'i': 1}
