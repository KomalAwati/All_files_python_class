path = r'D:\PYTHON\Python Class\Day9 30th-31st May\access-log.txt'
#**1. Write a program to find the length of the string without using inbuilt function (len)**

string = 'Komal'
count = 0
for _ in string:
    count += 1
print(count)#5


#**2. Write a program to reverse a string without using any inbuilt functions.**

string = 'Komal'
res = string[::-1]
print(res) #lamoK


#**3. Write a program to replace one string with another. e.g. "Hello World" replaces "World" with "Universe".**


string = 'Hello World'
old = 'World'
new = 'Universe'
words = string.split()
for word in words:
    if word == old:
        print(word + ' ' + new)



#**4. How to convert a string to a list and vice-versa.**

string = 'Hello World'
words = string.split()
print(words)
res = ' '.join(words)
print(res)


#**5. Convert the string "Hello welcome to Python" to a comma separated string.**

string = 'Hello World'
words = string.split()
print(words)
res = ' '.join(words)
print(res)


#**6. Write a program to print alternate characters in a string.**

string = 'Komal'
res = string[::2]
print(res) #Kml

#**7. Write a Program to print ascii values of the characters present in a string.**

string = 'Komal'
for char in string:
    print(ord(char))


#**8. Write a function to convert upper case to lower case and vice-versa without using inbuilt methods.**

def convert(string):
    res = []
    for char in string:
        temp = ord(char)
        if temp in range(97, 123):
            res.append(chr(temp - 32)) #LLO
        elif temp in range(65, 91):
            res.append(chr(temp + 32)) #he
    return "".join(res)
print(convert("HEllo"))
        
    
#**9. Write a program to swap two numbers without using the 3rd variable.**

a = 10
b = 20

a, b = b, a

print(a)
print(b)


#**10. Write a program to merge two different lists.**

l1= [1,2,3]
l2 = [4,5,6]
res = l1 + l2
res1 = [*l1, *l2]
print(res)
print(res1)
