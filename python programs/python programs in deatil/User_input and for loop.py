# Python program to calculate cube of given number
 
# take input a number from user
#num = int(input("Enter an any number: "))
 
# calculate cube using * operator
#cb = num*num*num
 
# display result
#print("Cube of {0} is {1} ".format(num, cb))

                                                    #format() method

#The format() method returns the formatted string.
# The format() method formats the specified value(s) and insert them inside the string's placeholder.\
#The placeholder is defined using curly brackets: {}

#Syntax
#string.format(value1, value2...)


#text = input("prompt")  # Python 3


                                                #FOR LOOP
#STATEMENTS ARE EXECUTED SEQUENTIALLY KNOWN AS FOR LOOP
#WE CAN ITERATE THE STRING,LIST,TUPLE AND SETS

#Print a "list" of items
'''
x=['Navin',6.2,1.5]
for i in x:
    print(i)'''
#O/p-
#Navin
#6.2
#1.5


#Print a "string" of items

'''
x = 'Komal'
for i in x:
    print(i)
'''

#O/p-
#K
#o
#m
#a
#l

#print(Specify the list in the for loop
'''for i in ['Komal',20,10.4]:
    print(i)'''
#O/p-
#Komal
#20
#10.4

                                            #Using Range in for loop

#Print a numbers from 0 to 9

'''for i in range(10):
    print(i)'''

#o/p -
'''
0
1
2
3
4
5
6
7
8
9
'''           
#print a value from 11 to 20
#(start_indx,end_index,step_size) #By default always step size's value will be 1
'''for i in range(11,21,1): 
    print(i)'''

#o/p -
'''
11
12
13
14
15
16
17
18
19
20
'''

#print a value from 11 to 20 which will be having te difference of two
'''
for i in range(11,20,2):
    print(i)
'''

#O/p -
'''
11
13
15
17
19
'''

#Print a numbers from 11 to 20 in the reverse order
'''for i in range(20,11,-1):
    print(i)'''

#O/p -
'''
20
19
18
17
16
15
14
13
12
11
'''

#Print a numbers from 11 to 20 with having 5 difference
'''
for i in range(11,20,5):
    print(i)
'''

#O/p -
'''
11
16
'''


                                            #for loop inside another for loop
#Print a number from 11 to 50 which are divisible by 5
'''
for i in range(1,51):
    if i % 5 == 0:
        print(i)
'''
#O/p -
'''
5
10
15
20
25
30
35
40
45
50
'''

#print a number from 1 to 20 but it should skip the no. which is divisible by 5
'''for i in range(1,21):
    if i%5!= 0:
        print(i)'''

#O/p -
'''
1
2
3
4
6
7
8
9
11
12
13
14
16
17
18
19
'''

#Print a number from 1 to 100 which are divisible by 10
'''for i in range(1,101):
    if i%10==0:
        print(i)'''
#O/p -
'''
10
20
30
40
50
60
70
80
90
100
'''

#Print a number from 1 to 10 but skip the numbers which are divisible by 2

'''for i in range(1,10):
    if i%2!=0:
        print(i)
        '''

#O/p -
'''
1
3
5
7
9
'''

#Print a number from 21 to 40 in reverse order whth their index value
'''for i in range(40,20,-1):
    print(i)'''
#O/p -

'''
40
39
38
37
36
35
34
33
32
31
30
29
28
27
26
25
24
23
22
21
'''

    














