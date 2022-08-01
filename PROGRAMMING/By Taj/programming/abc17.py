#  check if the given string is palindrome or not without using slicing method

def palindrome(string):
    res = ""
    for char in string:
        res = char + res
    if res == string:
        return f"{string} is palindrome"
    return f"{string} is not palindrome"

print(palindrome("mom"))

stri = 'momy'
for char in range(len(stri)):
    print(stri[char])

