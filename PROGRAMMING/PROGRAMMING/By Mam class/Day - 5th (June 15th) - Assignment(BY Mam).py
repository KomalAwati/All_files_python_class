# Program - 1st
# Python code to demonstrate
# sum of list of list
# using naive method

L = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
sum_internal = 0
for i in L: #[1, 2, 3]
    for j in i: #1 (3 iteration)
        sum_internal += j

#O/p -
#sum_internal      
#45
#*******************************************************************************************
'''
L = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
res = []
for i in L: #[1, 2, 3]
    sum_internal = 0
    for j in i: #1 (3 iteration)
        sum_internal += j
    res.append(sum_internal)
'''
#O/p -
#sum_internal 
#24

#*******************************************************************************************
#sum()
'''
L = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
res1 = []
for i in L: #[1, 2, 3](nested list)
    sum_internal = 0
    for j in i: #1 (3 iteration)
        sum_internal += j
    res1.append(sum_internal)
    
#sum()
for i in L:
    res1.append(sum(i))
'''


'''
sum(l)
no
sum([1,2,3])
6
'''
#*******************************************************************************************
#Using List Comprehension
#comp

#res2 = [sum(i) for i in L]

#*******************************************************************************************
# Program - 2nd
#Adding entire list

#Method - 1st
'''

l = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
sum_external = 0

for i in L:
    for j in i:
        sum_external += j
'''
#*******************************************************************************************
#Method - 2nd
'''
l = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
res2 = sum([sum(i) for i in l])
'''
#O/p -
#res2
#45

#*******************************************************************************************
#*******************************************************************************************

# Program - 3rd
# Python program to print
# duplicates from a list
# of integers

#Method 1: Using count() method
'''
names = [1, 2, 1, 2, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 9]
for name in set(names):
    if names.count(name) > 1:
        print(name)
'''

#O/p
'''
1
2
5
9
'''
#*******************************************************************************************
#Method 2: Without inbuilt method
'''
names = [1, 2, 1, 2, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 9]
res = []
dup = set()
for name in names:
    if name not in res:
        res.append(name)
    else:
        print(name) #dup.add(name)
'''

#O/p
'''
1
2
1
1
2
5
9
'''
#*******************************************************************************************
#Program 5th
# Python program to find the most common words

def most_frequent(List):
    counter = 0
    num = List[0]
     
    for i in List:
        curr_frequency = List.count(i)
        if(curr_frequency> counter):
            counter = curr_frequency
            num = i
 
    return num
 
List = [1, 2, 1, 2, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 9]
print(most_frequent(List))
#*******************************************************************************************
'''
#Using Defaultdict'
from collections import defaultdict

dd = defaultdict(int)

for word in words:
    dd[word] += 1

sorted(d.items(), key= lambda item : item[-1])
'''
#*******************************************************************************************
#Using Counter
'''
from collections import Counter
c = Counter(words) 
c.most_common() #returns list of tuples
most_occur = c.most_common(1) #returns first most common word
print(most_occur)
'''
