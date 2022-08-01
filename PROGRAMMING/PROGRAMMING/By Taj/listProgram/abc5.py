
#  prime number
num = 50
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("number is not a prime")
            break
    else:
        print("number is a prime")
