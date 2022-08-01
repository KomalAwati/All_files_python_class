#1
#Sort a list based on the reversed order
names = ['apple', 'google', 'yahoo', 'amazon', 'facebook', 'instagram', 'microsoft']
print(names[::-1])
#['microsoft', 'instagram', 'facebook', 'amazon', 'yahoo', 'google', 'apple']

#*************************************************************************************************
#2
#Sort a list based on their length
names = ['apple', 'google', 'yahoo', 'amazon', 'facebook', 'instagram', 'microsoft']
print(names.sort(key=len))

#['microsoft', 'instagram', 'facebook', 'amazon', 'yahoo', 'google', 'apple']

#*************************************************************************************************
# sort based on the length
words = ["yahoo", "instagram", "google", "flipkart", "walmart", "apple"]
print(sorted(words, key=len))

# sort based on last character of the elements in the list
def last_item(word):
    return word[-1]

last = lambda word: word[-1]
print(sorted(words, key=last))

# sorting a dictionary
d = {"4": "walmart", "1": "apple", "7": "instagram", "3": "yahoo"}

# sorting based on keys
print(sorted(d))
print(sorted(d.keys()))
print(sorted(d.items()))

# sorting based on values

print(sorted(d.values()))

def values_(item):
    return item[-1]

print(sorted(d.items(), key=values_))
print(sorted(d.items(), key=lambda item: item[-1]))

# sort the dictionary based on length of the key
d = {"ACME": 45.23, "AAPL": 612.78, "IBM": 205.55, "FB": 10.75, "HPQ": 37.20}
res = sorted(d.items(), key=lambda item: len(item[0]))
# print(dict(res))

# sort the dictionary based on last character of the key
d = {"ACME": 45.23, "AAPL": 612.78, "IBM": 205.55, "FB": 10.75, "HPQ": 37.20}
res = sorted(d.items(), key=lambda item: item[0][-1])
# print(dict(res))

# sort based on first character of value
d = {"Bangalore": "Traffic", "Mysore": "Palace", "Dharwad": "peda", "Bagalkot": "caves"}
res = sorted(d.items(), key=lambda item: item[1][0])
# print(dict(res))

# sort based on length of values
d = {"Bangalore": "Traffic", "Mysore": "Palace", "Dharwad": "peda", "Bagalkot": "caves"}
res = sorted(d.items(), key=lambda item: len(item[1]))
# print(dict(res))

#Anagram

def anagram(string1, string2):
    return sorted(string1) == sorted(string2)
# print(anagram("tea", "teaa"))


# grouping anagrams
words = ["tea", "eat", "silent", "hello", "listen", "ate"]

d = {}

for word in words:
    key = ''.join(sorted(word))
    if key not in d:
        d[key] = [word]
    else:
        d[key].append(word)
print(d)


#{'aet': ['eat', 'ate', 'tea'], 'eilnst': ['silent', 'listen'], 'ehllo': ['hello']}

# longest word
words = ["yahoo", "instagram", "google", "flipkart", "walmart", "apple"]
longest_word = ""

for word in words:
    if len(word) > len(longest_word):
        longest_word = word
print(longest_word)

# to print the longest non repeated word in the sentence

sentence = "python is a programming language and programming is fun"
words = sentence.split()
d = {}

d = {word: len(word) for word in words if words.count(word) == 1}
res = sorted(d.items(), key=lambda item: item[-1])
# print(res[-1])

# create a dictionary with word and length pair and get the longest and smallest words along with its length
sentence = "Today is Holi but still we are in class even afternoon we will be in class"
words = sentence.split()
d = {}

for word in words:
    if len(word) not in d:
        d[len(word)] = [word]
    else:
        d[len(word)] += [word]      # d[len(word)].append(word)
# print(d)

res = sorted(d.items())
smallest, *rest, longest = res
# print(smallest)
# print(longest)

# to print the most common word in the list

words = ["apple", "google", "gmail", "google", "apple", "google", "flipkart"]
d = {}

for word in words:
    if word not in d:
        d[word] = 1
    else:
        d[word] += 1
print(d)

res = sorted(d.items(), key=lambda item: item[1])
least_common, *rest, most_common = res
print(most_common)

# using Counter
from collections import Counter
words = ["apple", "apple", "google", "gmail", "google", "apple", "google", "flipkart"]
c = Counter(words)
print(c)
print(c.most_common())


