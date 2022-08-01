#   replace all vowels in the string to   *  
def replace(string):
    res = ""
    for char in  string:
        if char in "aeiou":
            res = res + "*"
        else:
            res = res + char
    return res

print(replace("hello world"))    #    h*ll* w*rld

def replace(string):
    res = ''
    for char in string:
        if char in 'aeiou':
            res = res + '*'
        else:
            res += char
    return res
print(replace("Hello"))
