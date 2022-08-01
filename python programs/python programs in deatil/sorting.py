
                                                    #NOTE

                                             #LAMBDA FUNCTION/EXPRESSION
#WHY WE USE????????? -----------------> WHEN WE WANT TO DECLAE IN THE SINGLE LINE WE MAKE USE OF LAMDA FUNCTION
#LAMBDA FUNCTION/EXPRESSION - IT IS ALSO CALLED AS INLINE FUNCTION / ANONYMOUS FUNCTION
#IT ALWAYS USE TO TAKE ONE ARGUMENT
#WHEN WE WANT TO DECLARE A FUNCTION INTO THE SINGLE LINE WE MAKE USE OF LAMDA FUNCTION


                                                    #Sorting List
#SORTED() IT WILL TAKE SOME ITERABLES
#SORTED() WE CAN SORT THE ITEMS BUT WITHOUT MODIFYING THE ORIGINAL STRING, IT WILL ALWAYS GIVE YOU THE NEW LIST
#The sort() method sorts the list ascending by default.
#Eg -
#list.sort(reverse=True|False, key=myFunc)
#reverse - Optional. reverse=True will sort the list descending. Default is reverse=False
#key - Optional. A function to specify the sorting criteria(s)


#Program - 1st
#Sort a list based on the length of the string

'''
items = ['bbbb', 'aaaaaa', 'yy', 'z', 'ccc']

def get_len(some_string):
    return len(some_string)

s_items = sorted(items, key=get_len)
print(s_items)

'''

#O/p-
#['z', 'yy', 'ccc', 'bbbb', 'aaaaaa']


#Program - 2nd
#Sort a list based on the last char of the string based on the alphabetica order

'''
items = ['bv', 'aw', 'dt', 'cu']

def get_last_chr(item):
    return item[-1]

s_items = sorted(items, key=get_last_chr)
print(s_items)'''

#O/p-
#['dt', 'cu', 'bv', 'aw']

#Program - 3rd
#Sort a list of the tuple based on the asecending order of the last no. of the given tuple
'''
temperatures = [('Bangalore', 25), ('Delhi', 35), ('Chennai', 37), ('Mumbai', 32)]

def get_temp(item):
    return item[-1]
s_temperature = sorted(temperatures, key=get_temp)
print(s_temperature)'''

#o/p-
#[('Bangalore', 25), ('Mumbai', 32), ('Delhi', 35), ('Chennai', 37)]

#***************************************************************************************************************

                                                        #SORTING A DICTIONARY
                                                    
#Program - 3rd
#Sort a dictionary based on the key values in ascending order
'''
prices = {'ACME': 45.23, 'AAPL': 612.78, 'IBM': 205.55, 'HPQ': 37.20, 'FB': 10.75 }

# item = ('ACME', 45.23)
def get_share_price(item):
    return item[-1]

# key_value_pairs = prices.items()
items = prices.items()
s_prices = sorted(items, key=get_share_price)
print(s_prices)
'''
#o/p -
#[('FB', 10.75), ('HPQ', 37.2), ('ACME', 45.23), ('IBM', 205.55), ('AAPL', 612.78)]

#Program -4th
#Sort a dictionary items based on the name,shares and price
'''portfolio = [
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

#print(by_price)
#[{'name': 'YHOO', 'shares': 45, 'price': 16.35}, {'name': 'FB', 'shares': 200, 'price': 21.09}, {'name': 'HPQ', 'shares': 35, 'price': 31.75},
# {'name': 'IBM', 'shares': 100, 'price': 91.1}, {'name': 'ACME', 'shares': 75, 'price': 115.65}, {'name': 'AAPL', 'shares': 50, 'price': 543.22}]

#Program - 4th
#Sort a dictionary based on the age,grade and name

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

print("Sorting a dictionary based on the 1st item: \n", by_first_item)
print('Sorting a dictionary based on the las item: \n' ,by_last_item)'''

#O/p -

#Sorting a dictionary based on the 1st item: 
 #[[2, 7], [3, 8], [4, 9], [7, 3], [8, 7], [9, 7]]
#Sorting a dictionary based on the las item: 
#[[7, 3], [2, 7], [8, 7], [9, 7], [3, 8], [4, 9]]

#***************************************************************************************************************
                                                  #SORTING A STRING      

#Program - 4th
#Sort a string based on the small string and also it should count the length of the string
'''
sentence = "This is a Programming language and Programming is fun"
words = sentence.split() #The split() method splits a string into a list.
                         #You can specify the separator, default separator is any whitespace.
word_len_pair = {  word: len(word) for word in words } len()    #It will return you length of the string
key_value_pairs = word_len_pair.items() #items- It will acccess the key and value pair values and print it in the form of tuple
by_len = sorted(key_value_pairs, key=lambda item: item[-1])  
print(by_len)
'''

#O/p-
#[('a', 1), ('is', 2), ('and', 3), ('fun', 3), ('This', 4), ('language', 8), ('Programming', 11)]

#Program - 5th
#Sort a string based on the small string and also it should count the length of the string
'''
sentence = "This is a Programming language and Programming is fun"
words = sentence.lower().split()
word_len_pair = {  word: len(word) for word in words if words.count(word) == 1 }
d = sorted(word_len_pair.items(), key=lambda item: item[-1])
print(d)'''
#O/p-
#[('a', 1), ('and', 3), ('fun', 3), ('this', 4), ('language', 8)]

#Program - 5th
#Print a most repeated word from the string
'''
sentence = "hi hello hi hello world hi universe hi world hello world hi world"
words = sentence.split()
word_count_pair = { word: words.count(word) for word in words }
most_repeated_word = sorted(word_count_pair.items(), key=lambda item: item[-1])[-1]
print(most_repeated_word)'''

#O/p-
#('hi', 5)

#Program - 6th
#Print a most repeated letter from the string
'''
sentence = 'hi hello hi hi hiiiiii'
char_count_pair = { letter: sentence.count(letter) for letter in sentence if letter.strip()}
by_letter_count = sorted(char_count_pair.items(), key=lambda item: item[-1])[-1]
print(by_letter_count )
'''

#O/p-
#('i', 9)

