# 2. Flipping keys and values of the dictionary using dict comprehension

d = {'a': 1, 'b': 2, 'c': 3}

flip_dict = {value: key  for key, value in d.items()  }

print(flip_dict)

# output:- {1: 'a', 2: 'b', 3: 'c'}
