#from collections import defaultdict
#1. Printing the line with line numbers
'''
with open(r'D:\PYTHON\python programs\info.txt') as f:
    for lineno, line in enumerate(f, start = 1):
        print(lineno, line, end = ' ')
'''

#2. Reading the file in reversed order
'''
with open(r'D:\PYTHON\python programs\info.txt') as f:
    for line in reversed(list(f)):
        print(line , end='')
'''
#3. Finding the length of each line in the text file
'''
with open(r'D:\PYTHON\python programs\info.txt') as f:
    for line in f:
        print(len(line))
'''
#4. Extracting IP addresses from log file.
'''
with open (r'D:\PYTHON\Python Class\Day9 30th-31st May\access-log.txt') as f:
    ip = []
    for line in f:
        line = line.strip()
        if line:
            parts= line.split()
            ip.append(parts[0])
print(ip)
'''     


#5. Counting number of occurrences of IP addresses in the log file.
'''
with open (r'D:\PYTHON\Python Class\Day9 30th-31st May\access-log.txt') as f:
    ip= []
    for line in f:
        line = line.strip()
        if line:
            parts = line.split()
            ip.append(parts[0])


d ={}
for item in ip:
    if item in d:
        d[item] += 1
    else:
        d[item] = 1
print(d)
'''

#Using defaultdit
'''
with open (r'D:\PYTHON\Python Class\Day9 30th-31st May\access-log.txt') as f:
    ip = []
    for line in f:
        line = line.strip()
        if line:
            parts = line.split()
            ip.append(parts[0])
d = defaultdict(int)
for item in ip:
        d[item] += 1
print(d)
'''
#6. Extracting Messages from sample.log
'''
with open(r'D:\PYTHON\Python Class\Day9 30th-31st May\sample.log') as f:
    messages = []
    for line in f:
        line = line.strip()
        if line:
            parts = line.split()
            messages.append(parts[2])
print(messages)'''

#['INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'TRACE', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'WARNING', 'INFO', 'TRACE', 'INFO', 'INFO', 'INFO', 'WARNING', 'INFO', 'TRACE', 'INFO', 'INFO', 'INFO', 'WARNING', 'INFO', 'TRACE', 'INFO', 'INFO', 'INFO', 'WARNING', 'INFO', 'TRACE', 'INFO', 'INFO', 'INFO', 'INFO', 'TRACE', 'INFO', 'INFO', 'INFO', 'INFO', 'TRACE', 'INFO', 'INFO', 'INFO', 'INFO', 'TRACE', 'INFO', 'INFO', 'INFO', 'TRACE', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'TRACE', 'EVENT', 'TRACE', 'INFO', 'TRACE', 'TRACE', 'TRACE', 'TRACE', 'TRACE', 'TRACE', 'EVENT', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'TRACE', 'INFO', 'TRACE', 'TRACE', 'TRACE', 'TRACE', 'TRACE', 'TRACE', 'TRACE', 'TRACE', 'INFO', 'TRACE', 'INFO', 'TRACE', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'EVENT', 'INFO', 'TRACE', 'INFO', 'TRACE', 'TRACE', 'TRACE', 'TRACE', 'TRACE', 'TRACE', 'EVENT', 'TRACE', 'INFO', 'TRACE', 'TRACE', 'TRACE', 'TRACE', 'INFO', 'TRACE', 'TRACE', 'TRACE', 'TRACE', 'TRACE', 'TRACE', 'TRACE', 'INFO', 'TRACE', 'INFO', 'TRACE', 'TRACE', 'TRACE', 'EVENT', 'TRACE', 'INFO', 'TRACE', 'TRACE', 'TRACE', 'TRACE', 'INFO', 'TRACE', 'TRACE', 'TRACE', 'TRACE', 'EVENT', 'TRACE', 'INFO', 'TRACE', 'TRACE', 'TRACE', 'TRACE', 'INFO', 'TRACE', 'TRACE', 'TRACE', 'TRACE', 'TRACE', 'TRACE', 'TRACE', 'INFO', 'TRACE', 'INFO', 'TRACE', 'TRACE', 'TRACE', 'EVENT', 'TRACE', 'INFO', 'TRACE', 'TRACE', 'TRACE', 'TRACE', 'INFO', 'TRACE', 'TRACE', 'TRACE', 'TRACE', 'EVENT', 'TRACE', 'INFO', 'TRACE', 'TRACE', 'TRACE', 'TRACE', 'INFO', 'TRACE', 'TRACE', 'TRACE', 'TRACE', 'TRACE', 'TRACE', 'TRACE', 'INFO', 'TRACE', 'INFO', 'TRACE', 'TRACE', 'TRACE', 'EVENT', 'TRACE', 'INFO', 'TRACE', 'TRACE', 'TRACE', 'TRACE', 'INFO', 'TRACE', 'TRACE', 'TRACE', 'TRACE', 'TRACE', 'EVENT', 'INFO', 'TRACE', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'EVENT', 'INFO', 'TRACE', 'TRACE', 'TRACE', 'TRACE', 'TRACE', 'TRACE', 'TRACE', 'EVENT', 'INFO', 'EVENT', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO']
#7. Counting Number of INFO, WARN, TRACE Messages.
'''
with open(r'D:\PYTHON\Python Class\Day9 30th-31st May\sample.log') as f:
    messages = []
    for line in f:
        line = line.strip()
        if line:
            parts = line.split()
            messages.append(parts[2])

d = {}
for item in messages:
    if item in d:
        d[item] += 1
    else:
        d[item] = 1
print(d)
'''
#8. Reading Countries from football.txt
'''
with open(r'D:\PYTHON\PROGRAMMING\Assignment Practice\football.txt') as log:
    countries=[]
    headers = next(log) #Skipping header
    for line in log:
        line = line.strip()
        if line:
            parts = line.split()
            countries.append(parts[1])
print(countries)

#Unique Countries
with open(r'D:\PYTHON\PROGRAMMING\Assignment Practice\football.txt') as log:
    unique = set()
    headers = next(log)
    for line in log:
        line = line.strip()
        if line:
            parts = line.split()
            unique.add(parts[1]) #Set has no attribute append it has add method
print(unique)
'''
            
#9. Counting total number of words present in a file
'''
with open(r'D:\PYTHON\Python Class\Day9 30th-31st May\sample.log') as f:
    words_count = 0
    for line in f:
        line = line.strip()
        if line:
            words = line.split()
            words_count += len(words)
print(words_count)
'''            
#10. Finding the line no of a particular word in a file.
'''
with open(r'D:\PYTHON\Python Class\Day9 30th-31st May\sample.log') as f:
    for lineno, line in enumerate(f, start=1):
        line = line.strip()
        if 'RSVP' in line:
            print(lineno, line)
'''            
#11. Printing 4 to 7th lines
'''
from itertools import islice

start = 4
end = 7

with open(r'D:\PYTHON\Python Class\Day9 30th-31st May\sample.log') as f:
    lines = islice(f, start-1, end)
    for line in lines:
        print(line)
'''          
#12. WAP to check if the file has even number of lines
'''
with open(r'D:\PYTHON\Python Class\Day9 30th-31st May\sample.log') as f:
    for line in f:
        line = line.strip()
        if line:
            if (len(line)%2)==0:
                print(line)
'''
#13. WAP to print only the lines which are starting with vowels
'''
with open (r'D:\PYTHON\Python Class\Day9 30th-31st May\java.txt') as f:
    for line in f:
        line = line.strip()
        if len:
            if line[0] in 'AEIOUaeiou':
                print(line)
'''
#14. WAP to count all the lowercase and uppercase letters in the file
'''
lower1 = 0
upper1 = 0
with open (r'D:\PYTHON\Python Class\Day9 30th-31st May\java.txt') as f:
    for line in f:
        for char in line:
            if ord('a')<= ord(char)<= ord('z'):
                lower1 += 1
            elif ord("A") <= ord(char)<= ord('Z'):
                upper1 += 1
print('Total upper :', upper1)
print('Total lower :', lower1)
'''
#Total upper : 25
#Total lower : 71

#15. WAP to create a dictionary with vowels and their count pair.
'''
with open (r'D:\PYTHON\Python Class\Day9 30th-31st May\java.txt') as f:
    d ={}
    for line in f:
        line = line.strip()
        if line:
            for word in line:
                if word in 'AEIOUaeiou':
                    if word in d:
                        d[word] += 1
                    else:
                        d[word] = 1
print(d)
'''
{'e': 10, 'o': 10, 'a': 9, 'u': 1, 'i': 2, 'A': 4, 'I': 3}
        


