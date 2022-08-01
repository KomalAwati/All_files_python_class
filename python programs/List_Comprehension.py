# [ expression   for item in iterable ]
#numbers = [1, 2, 3, 4, 5]

'''
squares = [ ]
for item in numbers:
    print(squares.append(item ** 2))


o/p-
None
None
None
None
None

# List Comprehension
_squares =[item ** 2 for item in numbers]
'''

'''
squares = []
for item in numbers:
    squares.append(item ** 2)
print(squares)


o/p-
[1, 4, 9, 16, 25]

'''


# List Comprehension

'''
_squares =[item ** 2 for item in numbers]
print(_squares)

o/p-
[1, 4, 9, 16, 25]

'''

# Print the even number

numbers = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
'''
evens = [ ]
for number in numbers:
    if number % 2 == 0:
        evens.append(number)
print(evens)
'''

'''
#Using Comprehension
_evens=[number for number in numbers if number % 2 == 0]
print(_evens)

o/p-
[2, 4, 6, 8, 10]

'''

# List of even numbers from 1 to 50
'''
evens = [ ]
for i in range(1, 51):
    if i % 2 == 0:
        evens.append(i)
print(evens)

o/p-

[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]

'''

#Using Comprehension
'''_evens = [  i  for i in range(1, 51) if i % 2 == 0 ]
print(_evens)

o/p-

[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]
'''

# using list comprehension
#_vowel_names = [  name  for name in names if name[0] in 'aeiou' ]

'''
languages = ['Python', 'Java', 'Perl', 'PHP', 'Python', 'JS', 'C++', 'JS', 'Python', 'Ruby']

p_languages = [ ]
for language in languages:
    if language[0] in 'P':
        p_languages.append(language)
print(p_languages)

o/p-

['Python', 'Perl', 'PHP', 'Python', 'Python']

'''




    

 

