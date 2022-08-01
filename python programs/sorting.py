#Sort a last Charerecters from the list
'''items = ['bv', 'aw', 'dt', 'cu']

def get_last_chr(item):
    return item[-1]
s_items = sorted(items, key=get_last_chr)'''

#o/p-
'''
s_items
['dt', 'cu', 'bv', 'aw']'''
                                            #SORTED
#The sorted() function returns a sorted list of the specified iterable object.
#You can specify ascending or descending order. Strings are sorted alphabetically, and numbers are sorted numerically.

                                            #LAMBDA
#A lambda function is a small anonymous function.
#A lambda function can take any number of arguments, but can only have one expression.
#Using a lambda - Sort a last Charerecters from the list


'''items = ['bv', 'aw', 'dt', 'cu']
s_items = sorted(items, key=lambda item: item[-1])
print(s_items)'''

O/p-

#['dt', 'cu', 'bv', 'aw']

'''
temperatures = [('Bangalore', 25), ('Delhi', 35), ('Chennai', 37), ('Mumbai', 32)]

def get_temp(item):
    return item[-1]

s_temperature = sorted(temperatures, key=get_temp)
print('Sorted a list of tuples based on the last numbers :\n ', s_temperature)
'''

#O/p-
#Sorted a list of tuples based on the last numbers :
#  [('Bangalore', 25), ('Mumbai', 32), ('Delhi', 35), ('Chennai', 37)]

#Sorted a dictionary based on the last values in ascending order
'''
prices = {'ACME': 45.23, 'AAPL': 612.78, 'IBM': 205.55, 'HPQ': 37.20, 'FB': 10.75 }

# item = ('ACME', 45.23)
def get_share_price(item):
    return item[-1]

# key_value_pairs = prices.items()
items = prices.items()
s_prices = sorted(items, key=get_share_price)
print(s_prices )

'''

#O/p-
#[('FB', 10.75), ('HPQ', 37.2), ('ACME', 45.23), ('IBM', 205.55), ('AAPL', 612.78)]

'''
portfolio = [
                {'name': 'IBM', 'shares': 100, 'price': 91.1 },
                {'name': 'AAPL', 'shares': 50, 'price': 543.22 },
                {'name': 'FB', 'shares': 200, 'price': 21.09},
                {'name': 'HPQ', 'shares': 35, 'price': 31.75},
                {'name': 'YHOO', 'shares': 45, 'price': 16.35},
                {'name': 'ACME', 'shares': 75, 'price': 115.65}
            ]

def get_name(item):
    return item['name']

def get_shares(item):
    return item['shares']

def get_price(item):
    return item['price']

def get_total(item):
    return item['price'] * item['shares']

by_name = sorted(portfolio, key=get_name)
by_shares = sorted(portfolio, key=get_shares)
by_price = sorted(portfolio, key=get_price)
by_total_cost = sorted(portfolio, key=get_total)
'''
#print(by_name)
#O/P - [{'name': 'AAPL', 'shares': 50, 'price': 543.22}, {'name': 'ACME', 'shares': 75, 'price': 115.65}, {'name': 'FB', 'shares': 200, 'price': 21.09}, {'name': 'HPQ', 'shares': 35, 'price': 31.75}, {'name': 'IBM', 'shares': 100, 'price': 91.1}, {'name': 'YHOO', 'shares': 45, 'price': 16.35}]

#print(by_shares)
#print(by_price)
#print(by_total_cost)

#OR
#USING LAMDA FUNCTION SORT A ITEMS

'''
by_name = sorted(portfolio, key=lambda item: item['name'])
by_shares = sorted(portfolio, key=lambda item: item['shares'])
by_price = sorted(portfolio, key=lambda item: item['price'])
by_total_cost = sorted(portfolio, key=lambda item: item['shares'] * item['price'])'''

'''
students = [
    {"name": "john", "grade": "A", "age": 26},
    {"name": "jane", "grade": "B", "age": 28},
    {"name": "dave", "grade": "B", "age": 22}
]

by_name = sorted(students, key=lambda student: student['name'])
by_grade = sorted(students, key=lambda student: student['grade'])
by_age = sorted(students, key=lambda student: student['age'])

items = [[2, 7], [7, 3], [3, 8], [8, 7], [9, 7], [4, 9]]

by_first_item = sorted(items, key=lambda item: item[0])
by_last_item = sorted(items, key=lambda item: item[-1])
print(by_first_item )
print(by_last_item)
'''

#O/p-
#[[2, 7], [3, 8], [4, 9], [7, 3], [8, 7], [9, 7]]
#[[7, 3], [2, 7], [8, 7], [9, 7], [3, 8], [4, 9]]

'''
sentence = "This is a Programming language and Programming is fun"
words = sentence.split()
word_len_pair = {  word: len(word) for word in words }
key_value_pairs = word_len_pair.items()
by_len = sorted(key_value_pairs, key=lambda item: item[-1])
print(by_len)'''

#O/p-
#[('a', 1), ('is', 2), ('and', 3), ('fun', 3), ('This', 4), ('language', 8), ('Programming', 11)]

