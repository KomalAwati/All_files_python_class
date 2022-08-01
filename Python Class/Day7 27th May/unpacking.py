point = (4, 5) 

# Indexing
x = point[0]
y = point[1]

# Tuple unpacking (Pythonic approach)
x, y = point

data = ['IBM', 50, 91.1, (2019, 7, 17)]

name = data[0]
shares = data[1]
price = data[2]
date = data[3]

# unpacking a list
name, shares, price, date = data

# unpacking a tuple
year, month, day = date

greet = "hello"

c1 = greet[0]
c2 = greet[1]
c3 = greet[2]
c4 = greet[3]
c5 = greet[4]

# unpacking a string
c1, c2, c3, c4, c5 = greet

names = ['apple', 'google', 'gmail', 'yahoo', 'facebook']


# for index, name in enumerate(names):
#     print(index, name)

a = [1, 2, 3, 4]
b = [5, 6, 7, 8]
c = [10, 20]

# for x, y, z in zip(a, b, c):
#     print(x, y, z)

d = {'one': 1, 'two':2, 'three': 3}

# for k, v in d.items():
#     print(k, v)

temperatures = {"Bangalore": (26, 32), "Chennai": (29, 35), "Delhi": (31, 36)}

# for city, temp in temperatures.items():
#     _min, _max = temp
#     print(city, _min, _max)

# for city, (_min, _max) in temperatures.items():
#     print(city, _min, _max)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# first_number = numbers[0]
# second_number = numbers[1]

first_number, second_number, *other_numbes = numbers

first_number, *middle_numbers, last_number = numbers

*rest, latest = numbers

first_numbers, *other_numbers = numbers