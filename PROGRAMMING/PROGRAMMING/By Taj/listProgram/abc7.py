l = []
num = 5

#   1
for i in range(2, num):
    if num % i == 0:
        l.append(False)
    else:
        l.append(True)

print(l)   #    [True, True, True]

#   2
res = []
for i in range(2, num):
    res.append(num % i)
print(res)    #   [1, 2, 1]

#  3
res = [num % i  for i in range(2, num)]
print(all(res))  #    True

