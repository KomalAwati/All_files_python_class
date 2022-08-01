#1. generate square numbers of given list
'''
l = [1, 2, 3, 4]

def square(_list):
    for i in _list:
        yield i ** 2
print(list(square(l)))
'''
#O/p-
#[1, 4, 9, 16]
        

#***********************************************************************************
#2. generate only the strings with odd length in the given list
'''
names = ["bob", "steve", "alex", "maya", "john"]

def odd_length(string):
    for i in string:
        if len(i) % 2 == 1:
            yield i
print(list(odd_length(names)))
'''
#['bob', 'steve']

#***********************************************************************************
#3. generate a tuple of only numeric values in the given list
#items = ["flipkart", 2021, "gmail", 1.2, [1, 2, 3], 2+3j, True]
'''
items = ["flipkart", 2021, "gmail", 1.2, [1, 2, 3], 2+3j, True]
def num_value(values):
    for i in values:
        if isinstance(i, (int,float,complex)) and not isinstance(i, bool):
            yield i
print(tuple(num_value(items)))
'''
#(2021, 1.2, (2+3j))

#***********************************************************************************
#4. generate a list -> if individual datatype, reverse it else keep it as it is
#items = ["flipkart", 2021, "gmail", 1.2, [1, 2, 3], 2+3j, True]
'''
items = ["flipkart", 2021, "gmail", 1.2, [1, 2, 3], 2+3j, True] #if you dont give bool also True will always use to consider the True as 1 
def rev_ind(lis):
    for i in lis:
        if isinstance(i, (int,float,complex,bool)):
            yield str(i)[::-1]
        else:
            yield i
print(list(rev_ind(items)))
'''
#['flipkart', '1202', 'gmail', '2.1', [1, 2, 3], ')j3+2(', 'eurT']
#***********************************************************************************
#5. write a generator function to yield even numbers in the range 1 - 50
'''
def even(maximum):
    for number in range(1, maximum+1):
        if(number % 2 == 0):
            yield '{0}'.format(number)
print(list(even(50)))
'''
#['2', '4', '6', '8', '10', '12', '14', '16', '18', '20', '22', '24', '26', '28', '30', '32', '34', '36', '38', '40', '42', '44', '46', '48', '50']

        
        
#***********************************************************************************

#6. write a generator function to yield the names starting with vowels in the given list
'''
names = ["john", "eve", "bob", "emma", "ana"]

def is_vowel(list):
    for name in names:
        if name[0] in 'aeiou':
            yield name
print(list(is_vowel(list)))
'''
#['eve', 'emma', 'ana']
            
#***********************************************************************************
#7. write a generator function and expression to yield length of each line in a file only if the line is not empty
'''
def len_():
    with open (r'D:\PYTHON\Python Class\Day9 30th-31st May\access-log.txt') as file:
        for line in file:
            line = line.strip()
            if line:
                yield len(line)
    
a=len_()
print(list(a))
'''
#[154, 171, 134, 147, 180, 186, 158, 171, 177, 169, 171, 134, 147, 177, 188, 176, 176, 177, 176, 176, 134, 138, 177, 177, 176, 154, 168, 158, 149, 163, 176, 175, 170, 170, 171, 170, 133, 126, 177, 170, 171, 190, 190, 175, 177, 133, 145, 177, 133, 175, 162, 177, 197, 175, 189, 186, 182, 192, 182, 198, 195, 186, 194, 183, 183, 186, 195, 189, 191, 189, 194, 195, 191, 191, 196, 189, 194, 176, 177, 134, 147, 177, 175, 165, 176, 319, 319, 175, 177, 175, 155, 175, 167, 176, 176, 176, 134, 144, 176, 172, 175, 132, 177, 133, 146, 173, 154, 171, 227, 175, 176, 124, 175, 158, 175, 165, 176, 175, 151, 133, 147, 153, 146, 138, 147, 155, 155, 155, 155, 155, 155, 149, 148, 154, 155, 155, 155, 154, 150, 141, 177, 175, 155, 176, 178, 170, 179, 178, 124, 176, 179, 177, 177, 177, 176, 176, 178, 171, 175, 176, 175, 176, 177, 176, 180, 175, 177, 177, 175, 170, 177, 239, 235, 248, 251, 283, 281, 273, 271, 271, 276, 273, 276, 277, 278, 177, 133, 124, 138, 176, 175, 176, 176, 178, 177, 133, 140, 175, 177, 177, 177, 175, 177, 177, 171, 170]

#41

numbers = [1, 2, 3, 4]
def power_(value, index):
    return value ** index
print(list(map(power_, numbers, range(len(numbers)))))

#[1, 2, 9, 64]

#42
numbers = [-2, 3, 5,-3]
print(list(map(abs, numbers)))
