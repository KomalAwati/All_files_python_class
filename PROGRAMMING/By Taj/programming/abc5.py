
#  Check list is palindrome or not

lst= ['mom', 'help', 'malayalam']
#palindrome = lambda string: f"{string} is palindrome" if string == string[::-1] else f"{string} is not palindrome"
#print(list(map(palindrome, lst)))


#  output:-  ['mom is palindrome', 'help is not palindrome', 'malayalam is palindrome']

palindrome = lambda string: f'{string} is palindrome' if string == string[::-1] else f'{string} is not palindrome'

print(list(map(palindrome, lst)))
