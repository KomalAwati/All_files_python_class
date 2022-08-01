# Group flower and Animals in the below list ?

items = ['lotus-flower', 'lilly-flower', 'cat-animal','sunflower-flower', 'dog-animal']

d= {}
for item in items:
    name, grp = item.split("-")
    if grp not in d:
        d[grp] = [name]
    else:
        # d[grp].append(name)  
         d[grp] += [name]

print(d)

# output:-   {'flower': ['lotus', 'lilly', 'sunflower'], 'animal': ['cat', 'dog']}
