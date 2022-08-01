# 3. Counting the number of each character in a String

my_string = 'guido van rossum'

d = {}
for char in my_string:
    if char not in d:
        d[char] = 1
    else:
        d[char] += 1

print(d)

# output:-  {'g': 1, 'u': 2, 'i': 1, 'd': 1, 'o': 2, ' ': 2, 'v': 1, 'a': 1, 'n': 1, 'r': 1, 's': 2, 'm': 1}
