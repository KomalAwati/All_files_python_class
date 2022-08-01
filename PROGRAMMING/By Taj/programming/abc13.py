#  write a function to convert a string into list and vise-versa
string = 'hello world'

# 1 converting string to list
words = string.split()
print(words)

# 2
def convert(sents):
    return list(sents)

list_ = convert(words)
print(list_)

# 3 converting list to string
def convert_list(lst):
    return " ".join(lst)

str_ = convert_list(words)
print(str_)