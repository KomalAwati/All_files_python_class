#  replacing one string with another string

string = "hello world"
words = string.split()
old_word = 'world'
new_word = 'universe'
res = ""
for word in words:
    if word == old_word:
        res += new_word + " "
    else:
        res += word + " "
print(res)