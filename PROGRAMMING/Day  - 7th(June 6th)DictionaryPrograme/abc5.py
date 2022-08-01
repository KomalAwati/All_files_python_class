
#  Grouping files with same extension

files = ['apple.txt', 'yahoo.pdf', 'gmail.pdf', 'google.txt', 'amazon.pdf', 'facebook.txt', 'flipkart.pdf']

d = {}
for file in files:
    name, ext = file.split('.')
    if ext not in d:
        d[ext] = [name]
    else:
        d[ext].append(name)

print(d)

# output:-  {'txt': ['apple', 'google', 'facebook'], 'pdf': ['yahoo', 'gmail', 'amazon', 'flipkart']}
