from collections import defaultdict

string = 'hello komal kow kour python coding practice is going on?'

words = string.split() #['Hello', 'Komal', 'how', 'your', 'python', 'coding', 'practice', 'is', 'going', 'on?']

d = {}

for word in words:
    if word[0] not in words:
        d[word[0]] = [word]
    else:
        d[word[0]] += [word]

#O/p-
#{'H': ['Hello'], 'K': ['Komal'], 'h': ['how'], 'y': ['your'], 'p': ['practice'], 'c': ['coding'], 'i': ['is'], 'g': ['going'], 'o': ['on?']}
        
#*******************************************************************************************************************************************
#Using defaultdict

sentence = 'hello komal kow kour python coding practice is going on?'
dd = defaultdict(list)
words = sentence.split()
for word in words:
    dd[word[0]].append(word)
print(dd)

#O/p-
#defaultdict(<class 'list'>, {'h': ['hello'], 'k': ['komal', 'kow', 'kour'], 'p': ['python', 'practice'], 'c': ['coding'], 'i': ['is'], 'g': ['going'], 'o': ['on?']})
