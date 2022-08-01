# 5. Dictionary of character and ascii value pairs

s = 'abcABC'
d = {}
for char in s:
    if char not in d:
        d[char] = ord(char)
    
print(d)

#  {'a': 97, 'b': 98, 'c': 99, 'A': 65, 'B': 66, 'C': 67}
