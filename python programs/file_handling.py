                                                                #File_Handling
#Program -1st
# Reading file without using Context manager
#"r" - Read - Default value. Opens a file for reading, error if the file does not exist
'''
f = open(r'D:\PYTHON\Python Class\Day9 30th-31st May\demo.txt', 'r') 
f_contents = f.read()
print(f_contents)
f.close()
'''

#Error
#If u just pass
#f = open('D:\PYTHON\Python Class\Day9 30th-31st May\access-log.txt', 'r')
#OSError: [Errno 22] Invalid argument: 'D:\\PYTHON\\Python Class\\Day9 30th-31st May\x07ccess-log.txt'



#To come out of this error we should make a use of '\\' - indiacates java
#or
#To come out of this error we should make a use of 'r' - here "r" indicates the raw string.

#*************************************************************************************************************

#Program -2nd
#Count the number of lines present in the string
# Reading file Using Context Manager (No need to close the file explicitly)

'''
with open(r'D:\PYTHON\Python Class\Day9 30th-31st May\demo.txt') as f:
    f_contents = f.readlines() # Returns a List
    for line in f_contents:
        print(line, end='')
    print('Number of lines in the file ', len(f_contents))
'''

#o/p-
#Hello Ishwary and Mayuri
#Hello Ishwary and Mayuri
#Hello Ishwary and Mayuri
#Hello Ishwary and Mayuri
#Hello Ishwary and Mayuri
#Number of lines in the file  5

#**************************************************************************************************************
#Program- 3rd
'''
with open(r'D:\PYTHON\Python Class\Day9 30th-31st May\demo.txt') as f:
    f_contents = f.read()
    print(f_contents , end=' ')
'''
#Passing the whitespace to the end parameter (end=‘ ‘) indicates that the end character has to be identified by whitespace and not a newline.

#**************************************************************************************************************
#Program- 4th

'''
with open(r'D:\PYTHON\Python Class\Day9 30th-31st May\demo.txt') as f:
    print(f.readline(), end='') # Reads one line at a time
    print(f.readline(), end='')
    print(f.readline(), end='')
'''

#O/p-
#Hello Ishwary and Mayuri
#Hello Ishwary and Mayuri
#Hello Ishwary and Mayuri

#**************************************************************************************************************
#Program- 5th
'''
with open(r'D:\PYTHON\Python Class\Day9 30th-31st May\demo.txt') as f:
    line = f.readline()
    while line:
        print(line, end='')
        line = f.readline()
        '''

#o/p-
#Hello Ishwary and Mayuri
#Hello Ishwary and Mayuri
#Hello Ishwary and Mayuri
#Hello Ishwary and Mayuri
#Hello Ishwary and Mayuri

#**************************************************************************************************************
#Program- 6th
'''
with open(r'D:\PYTHON\Python Class\Day9 30th-31st May\demo.txt') as f:
    for line in f: # Loads only one line at a time and prints the line
        print(line, end='')
        '''

#o/p-
#Hello Ishwary and Mayuri
#Hello Ishwary and Mayuri
#Hello Ishwary and Mayuri
#Hello Ishwary and Mayuri
#Hello Ishwary and Mayuri

#***************************************************************************************************************
#Program- 7th
# Reading 10 characters at a time
'''
size_to_read = 10
with open(r'D:\PYTHON\Python Class\Day9 30th-31st May\demo.txt') as f:
    f_contents = f.read(size_to_read)
    print(f_contents, end='')
    f_contents = f.read(size_to_read)
    print(f_contents, end='')

'''
#o/p-
#Hello Ishwary and Ma

#***************************************************************************************************************
#Program- 8th
#Printing the line's with line numbers

'''
with open(r'D:\PYTHON\Python Class\Day9 30th-31st May\demo.txt') as f:
    for linenumber, line in enumerate(f, start=1):
        print(linenumber, line, end='')
'''

#***************************************************************************************************************
#Program- 9th
# Reading the file in reversed order
'''

with open(r'D:\PYTHON\Python Class\Day9 30th-31st May\demo.txt') as f:
    for line in reversed(list(f)):
        print(line, end='')
'''
#O/p-
'''
Hello Ishwary and Mayuri Komal
Hello Ishwary and Mayuri
Hello Ishwary and Mayuri
Hello Ishwary and Mayuri
Hello Ishwary and Mayuri
'''
#***************************************************************************************************************
#Program- 10th
#Finding the length of each line in the text file
'''
with open(r'D:\PYTHON\Python Class\Day9 30th-31st May\demo.txt') as f:
    for line in f:
        print(len(line))
        '''

#O/p-
#25
#25
#25
#25
#31

#***************************************************************************************************************
#Program- 10th
## Exercises:
# 1. Extracting IP addresses from log file
'''with open(r'D:\PYTHON\Python Class\Day9 30th-31st May\access-log.txt') as f:
    ip = []
    for line in f:
        line = line.strip()
        if line:
            parts = line.split()
            ip.append(parts[0])
print(ip)'''


#O/p-

'''
['67.218.116.165', '66.249.71.65', '65.55.106.183', '65.55.106.183', '66.249.71.65', '66.249.71.65', '66.249.65.12', '66.249.65.12', '66.249.65.12', '66.249.65.12', '66.249.65.12', '65.55.106.131', '65.55.106.131', '66.249.65.12', '66.249.65.12', '66.249.65.12', '66.249.65.12', '66.249.65.12', '66.249.65.12', '66.249.65.12', '65.55.106.186', '65.55.106.186', '66.249.65.12', '66.249.65.12', '66.249.65.12', '74.52.245.146', '74.52.245.146', '66.249.65.43', '66.249.65.43', '66.249.65.43', '66.249.65.12', '66.249.65.12', '66.249.65.12', '66.249.65.12', '66.249.65.12', '66.249.65.12', '65.55.207.25', '65.55.207.25', '66.249.65.12', '66.249.65.12', '66.249.65.12', '66.249.65.12', '66.249.65.12', '66.249.65.12', '66.249.65.12', '65.55.207.94', '65.55.207.94', '66.249.65.12', '65.55.207.71', '66.249.65.12', '66.249.65.12', '66.249.65.12', '98.242.170.241', '66.249.65.38', '66.249.65.38', '66.249.65.38', '66.249.65.38', '66.249.65.38', '66.249.65.38', '66.249.65.38', '66.249.65.38', '66.249.65.38', '66.249.65.38', '66.249.65.38', '66.249.65.38', '66.249.65.38', '66.249.65.38', '66.249.65.38', '66.249.65.38', '66.249.65.38', '66.249.65.38', '66.249.65.38', '66.249.65.38', '66.249.65.38', '66.249.65.38', '66.249.65.38', '66.249.65.38', '66.249.65.38', '66.249.65.38', '65.55.207.126', '65.55.207.126', '66.249.65.38', '66.249.65.38', '66.249.65.38', '66.249.65.38', '82.34.9.20', '82.34.9.20', '66.249.65.38', '66.249.65.38', '66.249.65.38', '66.249.65.38', '66.249.65.38', '66.249.65.38', '66.249.65.38', '66.249.65.38', '66.249.65.38', '65.55.106.155', '65.55.106.155', '66.249.65.38', '66.249.65.38', '66.249.65.38', '66.249.65.38', '66.249.65.38', '65.55.207.77', '65.55.207.77', '66.249.65.38', '67.218.116.165', '66.249.65.38', '208.80.193.28', '66.249.65.38', '66.249.65.38', '66.249.65.38', '66.249.65.38', '66.249.65.38', '66.249.65.38', '66.249.65.38', '66.249.65.38', '66.249.65.38', '89.248.172.58', '89.248.172.58', '89.248.172.58', '89.248.172.58', '89.248.172.58', '89.248.172.58', '89.248.172.58', '89.248.172.58', '89.248.172.58', '89.248.172.58', '89.248.172.58', '89.248.172.58', '89.248.172.58', '89.248.172.58', '89.248.172.58', '89.248.172.58', '89.248.172.58', '89.248.172.58', '89.248.172.58', '89.248.172.58', '89.248.172.58', '89.248.172.58', '66.249.65.38', '66.249.65.38', '66.249.65.38', '66.249.65.38', '66.249.65.38', '66.249.65.38', '66.249.65.38', '66.249.65.38', '66.249.65.38', '66.249.65.38', '66.249.65.38', '66.249.65.38', '66.249.65.38', '66.249.65.38', '66.249.65.38', '66.249.65.38', '66.249.65.38', '66.249.65.38', '66.249.65.38', '66.249.65.38', '66.249.65.38', '66.249.65.38', '66.249.65.38', '66.249.65.38', '66.249.65.38', '66.249.65.38', '66.249.65.38', '66.249.65.38', '66.249.65.38', '67.195.112.35', '67.195.112.35', '67.195.112.35', '67.195.112.35', '67.195.112.35', '67.195.112.35', '67.195.112.35', '67.195.112.35', '67.195.112.35', '67.195.112.35', '67.195.112.35', '67.195.112.35', '67.195.112.35', '67.195.112.35', '67.195.112.35', '67.195.112.35', '66.249.65.38', '65.55.207.50', '65.55.207.50', '65.55.207.50', '66.249.65.38', '66.249.65.38', '66.249.65.38', '66.249.65.38', '66.249.65.38', '66.249.65.38', '65.55.215.75', '65.55.215.75', '66.249.65.38', '66.249.65.38', '66.249.65.38', '66.249.65.38', '66.249.65.38', '66.249.65.38', '66.249.65.38', '66.249.65.38', '66.249.65.38']
'''

#***************************************************************************************************************
#Program- 11th
# most standard way of reading files
'''
with open(r'D:\PYTHON\Python Class\Day9 30th-31st May\access-log.txt', 'r') as f:
    ip_address = [ ]
    for line in f:
        line = line.strip()
        parts = line.split()
        ip_address.append(parts[0])
print('List_items :', ip_address)
print('\n')
    

count = { }
for item in ip_address:
    if item in count:
        count[item] += 1
    else:
        count[item] = 1
print('Dictionary : ', count)
print('\n')

# sort the dictionary based on values

by_count = sorted(count.items(), key=lambda item: item[-1])
most_visited_ip = by_count[-3:]
least_visited_ip = by_count[:3]
print('most_visited_ip : ' , most_visited_ip)
print('least_visited_ip : ' , least_visited_ip)
print('\n')


#O/p-
#most_visited_ip :  [('89.248.172.58', 22), ('66.249.65.12', 32), ('66.249.65.38', 100)]
#least_visited_ip :  [('65.55.207.71', 1), ('98.242.170.241', 1), ('208.80.193.28', 1)]

unique_ip = [ ]
for item in ip_address:
    if item not in unique_ip:
        unique_ip.append(item)
print('unique_ip : ' , unique_ip)
'''

#O/p -

                                                                                #WRITTING THE FILE

#Program- 11th
#Creating the file and adding the data into it in the string format
#unique_ip1 = ['67.218.116.165', '66.249.71.65', '65.55.106.183', '66.249.65.12', '65.55.106.131', '65.55.106.186', '74.52.245.146', '66.249.65.43', '65.55.207.25', '65.55.207.94', '65.55.207.71', '98.242.170.241', '66.249.65.38', '65.55.207.126', '82.34.9.20', '65.55.106.155', '65.55.207.77', '208.80.193.28', '89.248.172.58', '67.195.112.35', '65.55.207.50', '65.55.215.75']
'''
with open(r".\\unique_ip1.txt", 'w') as fw:
    for item in unique_ip1:
        fw.write(item)
        fw.write("\n")

with open(r".\\unique_ip1.txt", 'r') as fw:
    print(fw.read())

'''
#O/p -

'''
67.218.116.165
66.249.71.65
65.55.106.183
66.249.65.12
65.55.106.131
65.55.106.186
74.52.245.146
66.249.65.43
65.55.207.25
65.55.207.94
65.55.207.71
98.242.170.241
66.249.65.38
65.55.207.126
82.34.9.20
65.55.106.155
65.55.207.77
208.80.193.28
89.248.172.58
67.195.112.35
65.55.207.50
65.55.215.75
'''

#Program- 12th
#Print a o/p in the below form -

# {"INFO": 100, "TRACE": 30, "WARNING": 26}

'''
with open(r'D:\PYTHON\Python Class\Day9 30th-31st May\sample.log', 'r') as log:
    messages = [ ]
    for line in log:
        line = line.strip()
        if line:
            parts = line.split()
            messages.append(parts[2])'''
#print(messages) #We will get the o/p in the list format


#O/p-
'''
['INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'TRACE', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'WARNING', 'INFO', 'TRACE', 'INFO', 'INFO', 'INFO', 'WARNING', 'INFO', 'TRACE', 'INFO', 'INFO', 'INFO', 'WARNING', 'INFO', 'TRACE', 'INFO', 'INFO', 'INFO', 'WARNING', 'INFO', 'TRACE', 'INFO', 'INFO', 'INFO', 'INFO', 'TRACE', 'INFO', 'INFO', 'INFO', 'INFO', 'TRACE', 'INFO', 'INFO', 'INFO', 'INFO', 'TRACE', 'INFO', 'INFO', 'INFO', 'TRACE', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'TRACE', 'EVENT', 'TRACE', 'INFO', 'TRACE', 'TRACE', 'TRACE', 'TRACE', 'TRACE', 'TRACE', 'EVENT', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'TRACE', 'INFO', 'TRACE', 'TRACE', 'TRACE', 'TRACE', 'TRACE', 'TRACE', 'TRACE', 'TRACE', 'INFO', 'TRACE', 'INFO', 'TRACE', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'EVENT', 'INFO', 'TRACE', 'INFO', 'TRACE', 'TRACE', 'TRACE', 'TRACE', 'TRACE', 'TRACE', 'EVENT', 'TRACE', 'INFO', 'TRACE', 'TRACE', 'TRACE', 'TRACE', 'INFO', 'TRACE', 'TRACE', 'TRACE', 'TRACE', 'TRACE', 'TRACE', 'TRACE', 'INFO', 'TRACE', 'INFO', 'TRACE', 'TRACE', 'TRACE', 'EVENT', 'TRACE', 'INFO', 'TRACE', 'TRACE', 'TRACE', 'TRACE', 'INFO', 'TRACE', 'TRACE', 'TRACE', 'TRACE', 'EVENT', 'TRACE', 'INFO', 'TRACE', 'TRACE', 'TRACE', 'TRACE', 'INFO', 'TRACE', 'TRACE', 'TRACE', 'TRACE', 'TRACE', 'TRACE', 'TRACE', 'INFO', 'TRACE', 'INFO', 'TRACE', 'TRACE', 'TRACE', 'EVENT', 'TRACE', 'INFO', 'TRACE', 'TRACE', 'TRACE', 'TRACE', 'INFO', 'TRACE', 'TRACE', 'TRACE', 'TRACE', 'EVENT', 'TRACE', 'INFO', 'TRACE', 'TRACE', 'TRACE', 'TRACE', 'INFO', 'TRACE', 'TRACE', 'TRACE', 'TRACE', 'TRACE', 'TRACE', 'TRACE', 'INFO', 'TRACE', 'INFO', 'TRACE', 'TRACE', 'TRACE', 'EVENT', 'TRACE', 'INFO', 'TRACE', 'TRACE', 'TRACE', 'TRACE', 'INFO', 'TRACE', 'TRACE', 'TRACE', 'TRACE', 'TRACE', 'EVENT', 'INFO', 'TRACE', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'EVENT', 'INFO', 'TRACE', 'TRACE', 'TRACE', 'TRACE', 'TRACE', 'TRACE', 'TRACE', 'EVENT', 'INFO', 'EVENT', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO', 'INFO']
'''
'''
message_count = { }
for message in messages:
    if message in message_count:
        message_count[message] += 1
    else:
        message_count[message] = 1
print(message_count)'''

#O/p-
#{'INFO': 147, 'TRACE': 119, 'WARNING': 4, 'EVENT': 13}

#Program- 13th
#Print a how many times each word has been repeated
'''
def count():
    with open(r'D:\PYTHON\Python Class\Day9 30th-31st May\demo.txt', 'r') as f:
        word_count = { }
        for line in f:
            line = line.strip()
            # if the string has atleast one character or if i have got a valid line
            if line:
                words = line.split()
                for word in words:
                    if word in word_count:
                        word_count[word] = word_count[word] + 1
                    else:
                        word_count[word] = 1
    return word_count
print(count())
'''

#O/p-
{'Hello': 5, 'Ishwary': 5, 'and': 5, 'Mayuri': 5, 'Komal': 1}

#Program- 14th
#Print the total number of words present in the file

'''
def word_count():
    """ Returns the total number of words present in the file"""
    _word_count = 0
    with open(r'D:\PYTHON\Python Class\Day9 30th-31st May\demo.txt') as f:
        for line in f:
            line = line.strip()
            if line:
                words = line.split()
                _word_count = _word_count + len(words)
    return _word_count
print(word_count())
'''

#O/p -
#21

#Program- 15th
#If python is present in the line it should be return in the form of index value and entire line

'''
with open(r'D:\PYTHON\Python Class\Day9 30th-31st May\demo.txt') as f:
    for index, line in enumerate(f, start=1):
        if "python" in line:
            print(f"{index} : {line}")

'''

#O/p -
#2 : Hello Ishwary and Mayuri python
#4 : Hello Ishwary and Mayuri python

#Program- 16th

'''   
with open(r".\\spam2.txt", 'x') as fw:  #"x" - Create - Creates the specified file, returns an error if the file exists
    fw.write("hello there")
    fw.write("\n")


with open(r'.\\spam2.txt') as fw:
    print(fw.read())

'''

#O/p -
#If file has already exists then it will return the FileExistsError
#: [Errno 17] File exists: '.\\\\spam1.txt'

#If file doesn't exists in the current directory it will returns string(hello there) o/p
#O/p -
#hello there


#Program- 17th
#Reading the two documents file parllely
'''
with open(r"D:\PYTHON\Python Class\Day9 30th-31st May\demo.txt") as f_java, open(r"D:\PYTHON\Python Class\Day9 30th-31st May\java.txt") as f_py:
    for java_line, py_line in zip(f_java, f_py):
        print(java_line, py_line)
'''

#O/p -
'''
Hello Ishwary and Mayuri
 Hello world welcome to java.

Hello Ishwary and Mayuri python
 Hello world welcome to java.

Hello Ishwary and Mayuri
 Hello universe hello java java.
'''

#Program- 18th
#Reading and writting the data
'''
with open(r"D:\PYTHON\Python Class\Day9 30th-31st May\java.txt") as fr, open(r".\\spam3.txt", 'w') as fw:
    for line in fr:
        if "WARNING" in line:
            fw.write(line)
'''
#O/p-
'''
Hello Ishwary and Mayuri
 Hello world welcome to java.

Hello Ishwary and Mayuri python
 Hello world welcome to java.

Hello Ishwary and Mayuri
 Hello universe hello java java.

Hello Ishwary and Mayuri python
 WARNING

Hello Ishwary and Mayuri Komal
 WARNING
'''

#Program- 19th

'''
with open(r'D:\PYTHON\Python Class\Day9 30th-31st May\sample.log', 'r') as fr:
    with open("info.txt", "w") as fw:
        for line in fr:
            if "INFO" in line:
                fw.write(line)

with open("info.txt") as fw:
    print(fw.read())

'''

#O/p-
#It will provide you the long o/p
    

        

        
    
             


    
        
        
            
         


 



