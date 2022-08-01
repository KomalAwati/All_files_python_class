#1
#  prime number
num = 50
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("number is not a prime")
            break
    else:
        print("number is a prime")
#2
#  prime number between 1 to 10      
for num in range(1, 10):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)
