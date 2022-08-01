

l = [1, 2, 3, 4, 5]
square = lambda num: num ** 2
print(square)   #return address
op = []
for number in l:
    res = square(number)
    op.append(res)
print(op)       #[1, 4, 9, 16, 25]

#  using map class
res = map(square, l)
print(list(res))