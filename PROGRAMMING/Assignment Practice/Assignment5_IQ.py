#1.
names = ['apple', 'google', 'yahoo', 'amazon', 'facebook', 'instagram', 'microsoft', 'zomato']
names_des = sorted(names,reverse = True)


#.8

prices = {'ACME': 45.23, 'AAPL': 612.78, 'IBM': 205.55, 'HPQ': 37.20, 'FB': 10.75 }
prices_sorted_key = sorted(prices.items(),key = lambda item: len(item[0]))
print(dict(prices_sorted_key))
#.9

prices = {'ACME': 45.23, 'AAPL': 612.78, 'IBM': 205.55, 'HPQ': 37.20, 'FB': 10.75 }
prices_sorted_value = sorted(prices.items(),key = lambda item: len(str(item[-1])))




#13

##def prime(number):
##    if number >1:
##        for  i in range(2,number):
##            if number%i ==0:
##                print("Not a prime")
##                break
##        else: print("number is prime")
##
##        
###prime_numbers = [ number if number == prime(number)  for number in range(1,51) ]
##p =[]
##for i in range(1,51):
##    if prime(i)== T

#.14

names = ['apple', 'google', 'yahoo', 'facebook', 'yelp', 'flipkart', 'gmail', 'instagram', 'microsoft']

names_rev_oddlength = [  ]
   
for name in names:
    if len(name)%2==0:
        names_rev_oddlength.append(name)
    else:
        names_rev_oddlength.append(name[::-1])
#********************LAMBDA FUNCTION********************
print("LAMBDA")        
#.17
add_15 = lambda number: number+15
print(add_15(30))

#.18
square = lambda number: number**2
cube = lambda number : number**3
print(square(9))
print(cube(4))

#.19

mul = lambda a,b : a*b
print(mul(3,4))

#20.
add = lambda a,b:a+b
print(add(12,90))
#21.
pre_exp = lambda a,b : a**2+b**2+2*a*b
print(pre_exp(6,8))

#22.

pre_exp1 = lambda a,b,c : 2*a+3*b+4*c
print(pre_exp1(6,8,7))

#23.

last_char = lambda num: num[-1]
print(last_char([23,2,67]))

#24.
check_even = lambda num: "EVEN" if num%2==0 else "Not even"
#25.
check_palindrome = lambda string:"Palindrome" if string==string[::-1] else "Not Palindrome"
print(check_palindrome("MOM"))
print(check_palindrome("DUMMY"))

#.18
#21.
#-----------------------------------




#---------------------------------------------------------
#############Sorted

#12. Anagram

def anagram(s1,s2):
    from time import time,sleep
    start = time()
    l_s1 = list(s1)
    l_s2 = list(s2)
    for item in l_s1:
            if item not in l_s2:
                print("Not Anagram")
                break
    else: print("Anagram")
    end = time()
    print(f"Time: {end-start}")
#13.Grouping Anagrams
##
##
        
    



#.15
numbers3 = [10,9,3,5,1,0.1]
max_num  = numbers3[0]
for number in numbers3:
    if number>max_num:
        max_num = number
print(max_num)


#.16
sentence = "Welcome to python programming and programming is fun"
s3 = { word:len(word) for word in sentence.split() if sentence.count(word)==1 }
s3_sorted = sorted(s3.items(),key = lambda item :item[-1])[-1]




#.17

sentence = "Welcome to python world and languageses and  then only programming is fun"
from collections import Counter
s1 = { word: len(word) for word in sentence.split() }
s1_sorted = sorted(s1.items(),key = lambda item:item[-1])




#.18
numbers1 = [1345,67,89,12,3456]
print(max(numbers1))

#---------------------
numbers2 = [10,9,3,5,1,0.1]
max_num  = numbers2[0]
for number in numbers2:
    if number>max_num:
        max_num = number
print(max_num)

#.20

sentence = "Welcome to python world and learn and  then only programming is fun"
from collections import Counter
s = { word: len(word) for word in sentence.split() }
s_sorted = sorted(s.items(),key = lambda item:item[-1])

#.21
numbers = [10,9,3,5,1,0.1]
least_num  = numbers[0]
for number in numbers:
    if number<least_num:
        least_num = number
print(least_num)


#22.
from collections import Counter

numbers =[2,3,1,2,4,1,8,7,3,1,1,1,7]
c = Counter(numbers)
#print(Counter(numbers))
print(c.most_common()[-1])
#********************FILTER*********************
#29.
_list = list(range(1,51))

def even_(num):
    if num%2==0:
        return num
print("*******")
print(list(filter(even_,_list)))

#30.
_list = list(range(1,51))
def odd_(num):
    if num%2==1:
        return num
print(list(filter(odd_,_list)))
#31.
names =['apple','google','yahoo','facebook','yelp','flipkart','gmail','instagram','microsoft']

def even_len(name):
    if len(name)%2==0:
        return name
print(list(filter(even_len,names)))

#32.
names1 =['laura','steve','bill','james','bob','greig','scott','alex','ive']
def vowel_start(name):
    if name[0] in 'aeiou':
        return name
print(list(filter(vowel_start,names1)))

#33.
numbers33 =[-2,-1,0,1,2,0.1]
def extract_pos(num):
    if num>0:
        return num
print(list(filter(extract_pos,numbers33)))

#34
_list = list(range(1,51))
def _prime(num):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:return num
            
    
print(list(filter(_prime,_list)))        

#35.
numbers35 =[-2,-1,0,1,2,0.1]

def extract_neg(num):
    if num<0:
        return num
print(list(filter(extract_neg,numbers35)))


#*******************MAPPING*************************
#38. Sq and cube of given interger list
numbers = [1,2,3,4,5,6]
sq = lambda num : num**2
cu = lambda num: num**3
print(list(map(sq,numbers)))
print(list(map(cu,numbers)))
#39.
#string=[('apple','a'),('gmail','l')]
def check_startchar(string,char):
    #string1,char = string[0]
    if string[0]==char:
        return True
    return False
#print(list(map(check_startchar,string)))
check= check_startchar('GOD','G')
print(check)
#.40
numbers40 =[-9,4,5,-6,-3]
def convert_neg_pos(num):
    if num<0:
        return abs(num)
print(list(map(convert_neg_pos,filter(convert_neg_pos,numbers40))))

#41.
numbers41 =[1,2,3,4,5]
def indices_power(num):
    res =[]
    for ind,num in enumerate(numbers41):
        res1 = num**ind
        res.append(res1)
    return res
print(list(map(indices_power,numbers41)))

#42.
numbers42 =[-9,4,5,-6,-3]
def s_p(num):
    res =0
    if num>0:
        s42 = num
        return s42
p=list(map(s_p,filter(s_p,numbers42)))
print(sum(p))

def s_n(num):
    res =0
    if num<0:
        s42 = num
        return sum([s42])
n =list(map(s_n,filter(s_n,numbers42)))
print(sum(n))











