#  reverse the string without using any in-built method

string = 'hello world'

#  1  slicing
res = string[::-1]
print(res)

#  2  using range()
for i in range(-1, -len(string)-1, -1):
    print(string[i], end = "")
print()        # this statement is used for take curser in next line

#  3  cancadination
res = ""
for char in string:
    res = char + res

print(res)