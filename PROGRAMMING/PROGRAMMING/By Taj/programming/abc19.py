def replace(string):
    res =""
    for char in string:
        if string.count(char) > 1:
            res = res + '-'
        else:
            res = res + char
    return res
print(replace('hello'))
