#Pgm - 1st
'''
for i in range(6):
    for j in range(i + 1):
        print('*', end = ' ')
    print()
#O/p

*
* *
* * *
* * * *
* * * * *
* * * * * *


for row in range(1, 6):
    print(' * ' * row)
'''
#Pgm - 2nd 
'''
for row in range(5, 0, -1):
    print(' * ' * row)
'''
#Pgm - 3rd
'''
for row in range(1, 6):
    print(f'{"* " * row:>10}')
print()
'''
'''
        *
      * *
    * * *
  * * * *
* * * * *
'''

#Pgm - 4th
'''
for row in range(5, 0, -1):
    print(f'{"* " * row:>10}')
'''
'''
* * * * *
  * * * *
    * * *
      * *
        *
'''

#Pgm - 5th
# centre justified triangle
"""
    *
   * *
  * * *
 * * * *
* * * * *
"""

'''
for row in range(1, 6):
    print(f'{"* " * row:^10}')

print()
'''

#Pgm - 6th
'''
for i in range(1, 6):
    for j in range(1,i+1):
        print(j, end=' ')
    print()

'''
'''
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
'''

#Pgm - 6th
"""
*
*
*
* *
*
* * *
*
* * * *
"""

for row in range(1, 5):
    print("*")
    print("* " * row)

print()