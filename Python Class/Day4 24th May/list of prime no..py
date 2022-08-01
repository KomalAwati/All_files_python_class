def is_prime(number):
    if number == 1:
        return False
    for i in range(2, number):
        if number % i == 0:
           return False
    return True

prime_numbers = [ ]

for i in range(1, 51):
    if is_prime(i):
        prime_numbers.append(i)

#Using Comprehension
        
