# WAP to get the indices of each item in the below list ?

names = ['apple', 'google', 'apple', 'yahoo', 'yahoo', 'google', 'gmail', 'gmail', 'gmail']
d= {}
for index, value in enumerate(names):
    if value not in d:
        d[value] = [index]
    else:
        # d[value].append(index)
        d[value] += [index]

print(d)

# output:-   {'apple': [0, 2], 'google': [1, 5], 'yahoo': [3, 4], 'gmail': [6, 7, 8]}
