#  Check string is palindrome or not

string = 'malayalam'
palindrome = lambda string: string == string[::-1]
print(palindrome(string)) 

#         or

def palind(name):
    if name == name[::-1]:
        print('String is palindrome')
    else:
        print('String is not palindrome')

palind(string)