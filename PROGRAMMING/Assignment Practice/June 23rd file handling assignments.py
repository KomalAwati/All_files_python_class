#1. Printing the line with line numbers
'''
with open(r'D:\PYTHON\python programs\info.txt') as f:
    for linenumber, line in enumerate(f, start=1):
        print(linenumber, line, end='')
'''
#**********************************************************************************************
#2. Reading the file in reversed order
'''
with open(r'D:\PYTHON\python programs\info.txt') as f:
    for line in reversed(list(f)):
        print(line, end='')
'''

#**********************************************************************************************
#3. Finding the length of each line in the text file
'''
with open(r'D:\PYTHON\python programs\info.txt') as f:
    for line in f:
        print(len(line))
'''
#********************************************************************************************** 
#4. Extracting IP addresses from log file.
'''
with open (r'D:\PYTHON\Python Class\Day9 30th-31st May\access-log.txt') as f:
    ip = []
    for line in f:
        line = line.strip()
        if line:
            parts = line.split()
            ip.append(parts[0])
print(ip)
'''    
#**********************************************************************************************
#5. Counting number of occurrences of IP addresses in the log file.
'''
with open (r'D:\PYTHON\Python Class\Day9 30th-31st May\access-log.txt') as f:
    ip = []
    for line in f:
        line = line.strip()
        if line:
            parts = line.split()
            ip.append(parts[0])
d = {}
for item in ip:
    if item in d:
        d[item] += 1
    else:
        d[item] = 1
print(d)
'''
#{'67.218.116.165': 2, '66.249.71.65': 3, '65.55.106.183': 2, '66.249.65.12': 32, '65.55.106.131': 2, '65.55.106.186': 2, '74.52.245.146': 2, '66.249.65.43': 3, '65.55.207.25': 2, '65.55.207.94': 2, '65.55.207.71': 1, '98.242.170.241': 1, '66.249.65.38': 100, '65.55.207.126': 2, '82.34.9.20': 2, '65.55.106.155': 2, '65.55.207.77': 2, '208.80.193.28': 1, '89.248.172.58': 22, '67.195.112.35': 16, '65.55.207.50': 3, '65.55.215.75': 2}


# Using defaultdict
'''
from collections import defaultdict
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
#defaultdict(<class 'int'>, {'67.218.116.165': 2, '66.249.71.65': 3, '65.55.106.183': 2, '66.249.65.12': 32, '65.55.106.131': 2, '65.55.106.186': 2, '74.52.245.146': 2, '66.249.65.43': 3, '65.55.207.25': 2, '65.55.207.94': 2, '65.55.207.71': 1, '98.242.170.241': 1, '66.249.65.38': 100, '65.55.207.126': 2, '82.34.9.20': 2, '65.55.106.155': 2, '65.55.207.77': 2, '208.80.193.28': 1, '89.248.172.58': 22, '67.195.112.35': 16, '65.55.207.50': 3, '65.55.215.75': 2})

# Using Counter Object
'''
from collections import Counter
with open (r'D:\PYTHON\Python Class\Day9 30th-31st May\access-log.txt') as f:
    ip = []
    for line in f:
        line = line.strip()
        if line:
            parts = line.split()
            ip.append(parts[0])
d = Counter(ip)
print(d)
#Counter({'66.249.65.38': 100, '66.249.65.12': 32, '89.248.172.58': 22, '67.195.112.35': 16, '66.249.71.65': 3, '66.249.65.43': 3, '65.55.207.50': 3, '67.218.116.165': 2, '65.55.106.183': 2, '65.55.106.131': 2, '65.55.106.186': 2, '74.52.245.146': 2, '65.55.207.25': 2, '65.55.207.94': 2, '65.55.207.126': 2, '82.34.9.20': 2, '65.55.106.155': 2, '65.55.207.77': 2, '65.55.215.75': 2, '65.55.207.71': 1, '98.242.170.241': 1, '208.80.193.28': 1})

'''
#***************************************************************************************************************************************************************
#6. Extracting Messages from sample.log
'''
with open(r'D:\PYTHON\Python Class\Day9 30th-31st May\sample.log') as log:
    for line in log:
        line = line.strip()
        if line:
            parts = line.split()
            print(parts[2])
'''

#***************************************************************************************************************************************************************
#7. Counting Number of INFO, WARN, TRACE Messages.
'''
with open(r'D:\PYTHON\Python Class\Day9 30th-31st May\sample.log') as log:
    messages = [ ]
    for line in log:
        line = line.strip()
        if line:
            parts = line.split()
            messages.append(parts[2])
print(messages)
message_count = { }
for message in messages:
    if message in message_count:
        message_count[message] += 1
    else:
        message_count[message] = 1
print(message_count)
'''
#{'INFO': 147, 'TRACE': 119, 'WARNING': 4, 'EVENT': 13}
#***************************************************************************************************************************************************************

#8. Reading Countries from football.txt
'''
with open(r'D:\PYTHON\PROGRAMMING\Assignment Practice\football.txt') as log:
    countries = []
    headers = next(log) # Skipping Header
    for line in log:
        if line.strip():
            parts = line.split('\t')
         countries.append(parts[1])
'''         '''  

with open(r'D:\PYTHON\PROGRAMMING\Assignment Practice\football.txt') as f:
    unique_countries = set()
    headers = next(log) # Skipping Header
    for line in f:
        if line.strip("\t"):
            parts = line.split()
            unique_countries.add(parts[1])
'''
#***************************************************************************************************************************************************************
#9. Counting total number of words present in a file
'''
words_count = 0
with open(r'D:\PYTHON\Python Class\Day9 30th-31st May\sample.log') as f:
    for line in f:
        if line.strip():
            words = line.split()
            #print(words)
            words_count += len(words)
print(words_count)
'''
#***************************************************************************************************************************************************************
            
#10. Finding the line no of a particular word in a file.
'''
with open (r'D:\PYTHON\Python Class\Day9 30th-31st May\sample.log') as f:
    for lineno , line in enumerate(f, start = 1):
        if line.strip():
            if 'RSVP' in line:
                print(lineno, line)
'''

#***************************************************************************************************************************************************************
#11. Printing 4 to 7th lines
'''
start = 4
end = 7

from itertools import islice
# islice
with open (r'D:\PYTHON\Python Class\Day9 30th-31st May\access-log.txt') as file:
    lines = islice(file, start-1, end)
    for line in lines:
        print(line)
'''       
#***************************************************************************************************************************************************************
#12. WAP to check if the file has even number of lines
'''
with open (r'D:\PYTHON\Python Class\Day9 30th-31st May\sample.log') as f:
    for line in f:
        if line.strip():
            if (len(line)%2)==0:
                print(line)
'''

#***************************************************************************************************************************************************************
#13. WAP to print only the lines which are starting with vowels
'''
with open (r'D:\PYTHON\Python Class\Day9 30th-31st May\java.txt') as f:
    for line in f:
        if line.strip():
            if line[0] in ('aeiouAEIOU'):
                print(line)
'''
#***************************************************************************************************************************************************************
#14. WAP to count all the lowercase and uppercase letters in the file
'''
lower_case = 0
upper_case = 0
with open (r'D:\PYTHON\Python Class\Day9 30th-31st May\java.txt') as f:
    for line in f:
        for char in line:
            if ord('a') <= ord(char) <= ord('z'):
                lower_case += 1
            elif ord('A') <= ord(char) <= ord(char):
                upper_case += 1
print(f'NO. of lowercase letters are : {lower_case}')
print(f'No. of uppercase letters are : {upper_case}')
'''
#O/p- 
#NO. of lowercase letters are : 71
#No. of uppercase letters are : 25
#***************************************************************************************************************************************************************
#15. WAP to create a dictionary with vowels and their count pair.
'''
with open (r'D:\PYTHON\Python Class\Day9 30th-31st May\java.txt') as file:
    word_count = {}
    # traversing through each line
    for line in file:
        if line.strip():
            # traversing through the words in a line
            for word in line:
                if word in 'AEIOUaeiou':
                    if word in word_count:
                        word_count[word] += 1
                    else:
                        word_count[word] = 1
'''
#{'e': 10, 'o': 10, 'a': 9, 'u': 1, 'i': 2, 'A': 4, 'I': 3}
                        
                    
                
                    
            
    print(word_count)

# WAP to read the random lines from file

#enumerate
#start= 1
#end = 100
'''
with open (r'D:\PYTHON\Python Class\Day9 30th-31st May\access-log.txt') as file:
    for line_no , line in enumerate(file, start=1):
        if start <= line_no <= end:
            print(line)
'''

#islice
'''
from itertools import islice
with open (r'D:\PYTHON\Python Class\Day9 30th-31st May\access-log.txt') as file:
    lines = islice(file, start-1, end)
    print(list(lines))
'''
#***************************************************************************************************************************************************************

#2. WAP TO READ THE 1st N LINES
'''
start = 0
end = 5

with open (r'D:\PYTHON\Python Class\Day9 30th-31st May\access-log.txt') as file:
    for line_no, line in enumerate(file, start):
        if start <= line_no <= end:
            print(line)
'''
#***************************************************************************************************************************************************************
#3. WAP TO READ THE LAST N LINES
'''
n = 3
from itertools import islice
with open (r'D:\PYTHON\Python Class\Day9 30th-31st May\access-log.txt') as file:
    lines_count = 0
    for _ in file:
        lines_count += 1
    print(lines_count)
    file.seek(0)
    lines = islice(file, lines_count - n, lines_count)
    print(list(lines))
'''
#206
#['66.249.65.38 - - [31/Jan/2010:20:17:07 +0200] "GET /browse/download_model/1800 HTTP/1.1" 200 14802 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"\n', '66.249.65.38 - - [31/Jan/2010:20:42:19 +0200] "GET /browse/one_node/1613 HTTP/1.1" 200 27080 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"\n', '66.249.65.38 - - [31/Jan/2010:21:08:00 +0200] "GET /browse/one_node/1892 HTTP/1.1" 200 1296 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"']


#Using deque
'''
n = 3
from collections import deque
with open (r'D:\PYTHON\Python Class\Day9 30th-31st May\access-log.txt') as file:
    lines = deque(file, n)
    print(list(lines))
'''
#['66.249.65.38 - - [31/Jan/2010:20:17:07 +0200] "GET /browse/download_model/1800 HTTP/1.1" 200 14802 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"\n', '66.249.65.38 - - [31/Jan/2010:20:42:19 +0200] "GET /browse/one_node/1613 HTTP/1.1" 200 27080 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"\n', '66.249.65.38 - - [31/Jan/2010:21:08:00 +0200] "GET /browse/one_node/1892 HTTP/1.1" 200 1296 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"']

#***************************************************************************************************************************************************************    


