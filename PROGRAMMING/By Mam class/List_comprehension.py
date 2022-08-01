#Pgm -1st
'''
l = [1,2,3,4]
l2 = []
for item in l:
    l2.append(item ** 2)
print(l2)
'''   

#s = [item **2 for item ** 2]

#Program
'''
for i in range(1,51): #
    print(i%2 == 0) #It will return true and false values

'''
#########################################################################################################################
#Pgm -2nd
'''
for i in range(1,51):#
    if i%2 == 0:
       print(i)
'''
#O/p -
'''
2
4
6
8
10
12
14
16
18
20
22
24
26
28
30
32
34
36
38
40
42
44
46
48
50
'''
'''
l = [i for i in range(1,51) if i%2 == 0]
print(l)
'''
#O/p-
#[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]

#########################################################################################################################
#Pgm -3rd
names = ['laura', 'steve', 'bill', 'james', 'bob', 'greig', 'scott', 'alex', 'ive']
'''
list =[]
for i in names:
    if i[0] in 'aeiou':
        list.append(i)
print(list) 

'''
#['alex', 'ive']
'''
list = [i for i in names if i[0] in 'aeiou']
print(list)
'''
#['alex', 'ive']       

#########################################################################################################################
#4. Filtering all the languages which starts with 'p'
'''
languages = ['Python', 'Java', 'Perl', 'PHP', 'Python', 'JS', 'C++', 'JS', 'Python', 'Ruby']

list = [i for i in languages if i[0] in 'P']

print(list)''' #['Python', 'Perl', 'PHP', 'Python', 'Python']

#########################################################################################################################
#5. Names starting with consonants in list 
'''
names = ['apple', 'google', 'yahoo', 'gmail', 'flipkart', 'instagram', 'microsoft']

list1 = [i for i in names if i[0] not in 'aeiou']
print(list1)
'''
#O/p -
#['google', 'yahoo', 'gmail', 'flipkart', 'microsoft']

#########################################################################################################################
#6. Filtering out those names which are less than 6 characters
'''
names = ['apple', 'google', 'yahoo', 'gmail', 'flipkart', 'instagram', 'microsoft']
l1 = []
for i in names:
    if len(i) < 6:
        l1.append(i)
print(l1)

#['apple', 'yahoo', 'gmail']

list = [l1 for i in names if len(i) < 6]
'''
#['apple', 'yahoo', 'gmail']

#########################################################################################################################
#7. Raise to the power of list index
#a = [1, 2, 3, 4, 5]
'''
list =[]

for index, item in enumerate(a):
    list.append(item ** index)
print(list) #[1, 2, 9, 64, 625]
'''
'''
list = [item ** index for index, item in enumerate(a)]
print(list)
[1, 2, 9, 64, 625]
'''
#########################################################################################################################
#8. Build a list of tuples with string and its length pair
#names = ['apple', 'google', 'yahoo', 'facebook', 'yelp', 'flipkart', 'gmail', 'instagram', 'microsoft']
'''
l = []
for name in names:
    l.append(name, len(name))
print(l)
'''
#[('apple', 5), ('google', 6), ('yahoo', 5), ('facebook', 8), ('yelp', 4), ('flipkart', 8), ('gmail', 5), ('instagram', 9), ('microsoft', 9)]
'''
list =[(name, len(name)) for name in names]
print(list)
'''
#[('apple', 5), ('google', 6), ('yahoo', 5), ('facebook', 8), ('yelp', 4), ('flipkart', 8), ('gmail', 5), ('instagram', 9), ('microsoft', 9)]

#########################################################################################################################
#9. Build a list with only with even length string
#names = ['apple', 'google', 'yahoo', 'facebook', 'yelp', 'flipkart', 'gmail', 'instagram', 'microsoft']
'''
l =[]
for name in names:
    if len(name)%2 == 0:
        l.append(name)
print(l)
'''
#O/p -
#['google', 'facebook', 'yelp', 'flipkart']
'''
list = [name for name in names if len(name)%2 == 0]
print(list)
'''
#O/p -
#['google', 'facebook', 'yelp', 'flipkart']

#########################################################################################################################
#10. List comprehension to sum the factorial of numbers from 1-5

#factorial no. - 5 = 1*2

#########################################################################################################################
#11. Reverse the item of a list if the item is of odd length string
'''
names = ['apple', 'google', 'yahoo', 'facebook', 'yelp', 'flipkart', 'gmail', 'instagram', 'microsoft']

list = [name[::-1] for name in names if len(name)%2 != 0]
print(list)
'''
#['elppa', 'oohay', 'liamg', 'margatsni', 'tfosorcim']

#########################################################################################################################
#12. Reverse the item of a list if the item is of odd length string otherwise keep the item as is!.
names = ['apple', 'google', 'yahoo', 'facebook', 'yelp', 'flipkart', 'gmail', 'instagram', 'microsoft']

list = [name if len(name)%2 == 0 else name[::-1] for name in names ]
print(list)

#['elppa', 'google', 'oohay', 'facebook', 'yelp', 'flipkart', 'liamg', 'margatsni', 'tfosorcim']

#########################################################################################################################
