#****************************************************************************************************
#Program - 1st
nums = [1,2,3,4,5]
'''
nums = [1,2,3,4,5]
for num in nums:
    print(num)
'''
#o/p -
'''
1
2
3
4
5
'''
#****************************************************************************************************
#Program - 2
'''
for num in nums:
    if num == 3:
        print("found")
    print(num)
'''
#o/p-
'''
1
2
found
3
4
5
'''
#****************************************************************************************************
#Program - 3
'''
for num in nums:
    if num == 3:
        print("found")
print(num)
'''
#o/p-
#found
#5
#****************************************************************************************************

                                                                #Iterator
#Iterator - Is an object that can return data at a time while iterating over it.
#Iterables - Anything you can loop over it is called as an iterables
#__iter__() - it will give you object of the iterator
#__next__() - It will give you the next value/object

#Program - 4
'''
nums = [1,2,3,4]

it = iter(nums)
print(it)
'''
#or
'''
nums = [1,2,3,4]

it = nums.__iter__() 
print(it)
'''
#o/p-
#<list_iterator object at 0x00000210218F4700>

#****************************************************************************************************
'''
nums = [1,2,3,4]

it = iter(nums) 
print(it.__next__()) #1
'''

#o/p-
#1
#****************************************************************************************************
'''
nums = [1,2,3,4]
it = iter(nums)
print(it.__next__())
print(it.__next__())
'''
#o/p-
#1
#2

#****************************************************************************************************
'''
nums = [1,2,3,4]
it = iter(nums)
print(it.__next__())
print(it.__next__())
print(next(it))
print(next(it))
'''
#o/p-
#1
#2
#3
#4
#****************************************************************************************************
'''
nums = [1,2,3,4]
it = iter(nums)
print(it.__next__())
print(it.__next__())
print(next(it))
print(next(it))

for i in nums:
    print(i)
'''
#O/p-
'''
1
2
3
4
1
2
3
4
'''
#******************************************************************************************************
#nums = [1,2,3,4]

'''
it = iter(nums)
print(it.__next__())
print(it.__next__())
print(next(it))
print(next(it))
'''

#or
'''
for it in nums:
    print(it)
'''
#******************************************************************************************************
#Creating own iterator
'''
class TopTen:
    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.num <= 10:
            value = self.num
            self.num += 1
            return value
        else:
            raise Exception
values = TopTen()
print(values.__next__())
print(values.__next__())
'''
#Or
'''
class TopTen:
    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.num <= 10:
            value = self.num
            self.num += 1
            return value
        else:
            raise StopIteration
      
values = TopTen()

for i in values:
    print(i)

'''
    
#O/p-
'''
1
2
3
4
5
6
7
8
9
10        
'''
#******************************************************************************************************
                                                            #Generator

#Use - It will fetch the particular element rest all the elements dont need to load into the memory
'''

def topten():
    
    yield 1
    yield 2

values = topten()
print(values.__next__())
print(values.__next__())
'''

#O/p -
#1
#2



'''                                        #OR
def topten():
    
    yield 1
    yield 2

values = topten()
for i in values:
    print(i)
'''

#O/p -
#1
#2
#**********************************************************************************************************
'''
def topten():
    n=1
    while n <= 10:
        sq = n * n
        yield sq
        n+=1
values = topten()

for i in values:
    print(i)
'''
#O/p -
'''
1
4
9
16
25
36
49
64
81
100
'''

    
