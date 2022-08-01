#[Expressions for item in iterable]

numbers = [1,2,3,4]
squares = []
for item in numbers:
    squares.append(item ** 2)

#List Comprehension
_squares = [item ** 2 for item in numbers]

numbers = [1,2,3,4,5]
evens = []
for number in numbers:
    if number % 2:
        evens.append(number)


