# Reverse the values in the dictionary if the value is of type string ?

d = {'a': "hello", 'b': 100, 'c': 10.1, 'd': 'world'}

# for key, value in d.items():
#     if isinstance(value, str):
#         d[key] = value[::-1]
#     else:
#         d[key] = value

# print(d)  #   {'a': 'olleh', 'b': 100, 'c': 10.1, 'd': 'dlrow'}

# 2
d1 = {key: value[::-1]  if isinstance(value, str) else value   for key, value in d.items()}
print(d1)

# output:-  
