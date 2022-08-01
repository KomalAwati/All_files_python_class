'''
row = 4
for i in range(4):
    c = 1
    print(c, end=' ')
    for j in range(3):
        c = c + 1
        print(c, end=' ')
        print('*', end=' ')
    print('\n')

n = 4

for x in range(1, n+1):
    for y in range(1, n + 1):
        print('*', end=' ')
    print()
        
    
'''
#Pgm -
'''
for i in range(1,5):
    for j in range(1,5):
        if i+j == 5:
            print("*", end= " ")
        else:
            print(j, end = " ")
    print()
'''
'''
1 2 3 * 
1 2 * 4 
1 * 3 4 
* 2 3 4
'''
#Pgm -

