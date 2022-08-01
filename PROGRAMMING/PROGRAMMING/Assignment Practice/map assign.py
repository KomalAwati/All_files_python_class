#Eg. POlymorphism
'''
names = ['alex', 'james', 'Komal', 'Divya']

char = 'j'

def search(name,ch = char): #make deafult argument
    return name[0] == ch

res = list(map(search, names))
print(res)

#it can take an argument which you are passing

'''
# WAP to raise the numbers in list to the power of their indices
'''
nums = [2,3,4,5,6]
#indices = [0,1,2,3,4] #(0 to len(nums)-1)
#indices = range(0, len(nums))
def power(item): #Tuple
    return item[1] ** item[0]
map(power, enumerate(num)) #whenever using enumerate you are passing list of tuple
'''
#or
'''
nums = [2,3,4,5,6]
indices = range(0, len(nums))
def power_(index, item):
    return item ** index

res = list(map(power_,indices , nums))
print(res)

#map(power_, indices, nums) #[1, 3, 16, 125, 1296]
'''

# WAP to convert -ve to +ve numbers in a list
'''
#sum of -ve to +ve numbers
l = [1, 4, 5, -2, 4, -6]
pos = lambda num: num > 0
neg = lambda num: num < 0

pos_num = sum(list(filter(pos, l)))
neg_num = sum(list(filter(neg, l)))

print(pos_num, neg_num)
'''


#Anagram
words = ['eat', 'silent', 'ate', 'tea', 'listen', 'hello']

d = {}

#O/p - {'aet': ['eat', 'ate', 'tea'], 'eilnst': ['silent', 'listen'], 'ehllo': ['hello']}

#Keys - list are not mutable so typecast it(Key must be immutable)

'''
for word in words:
    key = ''.join(sorted(word))
    if key not in d:
        d[key] = [word]
    else:
        d[key].append(word)
print(d)
'''
#{'aet': ['eat', 'ate', 'tea'], 'eilnst': ['silent', 'listen'], 'ehllo': ['hello']}



