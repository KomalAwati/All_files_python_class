#  print only even numbers

list_ = list(range(1, 21))
def evens(num):
    if num % 2 == 0:
        return num
print(list(map(evens, list_)))

#   output:-   [None, 2, None, 4, None, 6, None, 8, None, 10, None, 12, None, 14, None, 16, None, 18, None, 20]

print(list(filter(evens, list_)))

#  output:-   [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]