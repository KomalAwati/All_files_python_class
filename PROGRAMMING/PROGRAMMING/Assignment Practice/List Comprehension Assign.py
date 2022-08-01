                                                                    #Assignments
#Using Comprehension
#1
#prime numbers
#A number that is divisible only by itself and 1 (e.g. 2, 3, 5, 7, 11).
#Normal program

#n = 50
#primes = []
'''
for i in range(2, n):
	for j in range(2, int(i ** 0.5) + 1):
 		if i%j == 0:
 			break
	else:
		primes.append(i)

print(primes)

'''
    
#Using list Comprehension
print([i for i in range(2, 50) if 0 not in [i%n for n in range(2, i)]])

#[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

   
#WAP to check wheather given no is Prime or not.
#Python program to check whether a number is  prime or not
'''
n = 5
if n > 1:
    for i in range(2, n):
        if n % i == 0:
            print("not prime")
    print("prime")


#Using function
def prime(n):
    for i in range(2, n):
        if n % i == 0:
            return f'{n} is not prime'
        return f'{n} is prime '
print(prime(8))
'''

#*****************************************************************************************************************

#2. Reverse the item of a list if the item is of odd length string
'''
names = ['apple', 'google', 'yahoo', 'facebook', 'yelp', 'flipkart', 'gmail', 'instagram', 'microsoft']

list = [name[::-1] for name in names if len(name)%2 != 0]
print(list)
'''
#['elppa', 'oohay', 'liamg', 'margatsni', 'tfosorcim']



#2.1. Reverse the item of a list if the item is of odd length string otherwise keep the item as is!

#NP
'''
names = ['apple', 'google', 'yahoo', 'facebook', 'yelp', 'flipkart', 'gmail', 'instagram', 'microsoft']

l1 = []
for word in names:
    if len(word) % 2 == 0:
        l1.append(word)
    else:
        l1.append(word[::-1])
print(l1)

#['elppa', 'google', 'oohay', 'facebook', 'yelp', 'flipkart', 'liamg', 'margatsni', 'tfosorcim']



#Using list Comprehension
l2 = [word if len(word) % 2 == 0 else word[::-1] for word in names]
print(l2)
#['elppa', 'google', 'oohay', 'facebook', 'yelp', 'flipkart', 'liamg', 'margatsni', 'tfosorcim']
'''

#*****************************************************************************************************************
    
