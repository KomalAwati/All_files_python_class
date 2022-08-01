#Program - 1st
#WAP to count the number of lines in the file without loading the file in the memory 
'''
with open (r'D:\PYTHON\python programs\info.txt') as file:
    count = 0
    for _ in file:
        count +=1
print(count)
'''
#147
#*****************************************************************
#Program - 2nd

#WAP TO COUNT THE NO. OF IP ADDRESS IN ACCESS LOG FILE
'''
with open (r'D:\PYTHON\Python Class\Day9 30th-31st May\access-log.txt') as file:
    d ={}
    for line in file:
        if line.strip():#Strip() - it will be stripping \n and whitespaces and also to remove nad check for blank space
            words = line.split()  #If you have blank space while splitting the line it will raise an index error exception #how to unpack to 1st elment #ip_, *words = line.split()
            ip_ = words[0]

            if ip_ not in d:
                d[ip_] =1
            else:
                d[ip_] +=1
    print(d)
'''

#O/P
#{'67.218.116.165': 2, '66.249.71.65': 3, '65.55.106.183': 2, '66.249.65.12': 32, '65.55.106.131': 2, '65.55.106.186': 2, '74.52.245.146': 2, '66.249.65.43': 3, '65.55.207.25': 2, '65.55.207.94': 2, '65.55.207.71': 1, '98.242.170.241': 1, '66.249.65.38': 100, '65.55.207.126': 2, '82.34.9.20': 2, '65.55.106.155': 2, '65.55.207.77': 2, '208.80.193.28': 1, '89.248.172.58': 22, '67.195.112.35': 16, '65.55.207.50': 3, '65.55.215.75': 2}

#Using dafult dict and counter


#*****************************************************************
#Program - 3rd
#Wap to print most repeated IP address along with its count

#d.items() - both will be given
'''
with open (r'D:\PYTHON\Python Class\Day9 30th-31st May\access-log.txt') as file:
    d ={}
    for line in file:
        if line.strip():#Strip() - it will be stripping \n and whitespaces and also to remove nad check for blank space
            words = line.split()  #If you have blank space while splitting the line it will raise an index error exception #how to unpack to 1st elment #ip_, *words = line.split()
            ip_ = words[0]

            if ip_ not in d:
                d[ip_] =1
            else:
                d[ip_] +=1
    print(d)
least, *rest, most = sorted(d.items(), key =lambda item : item[-1])
'''

#print("Most repeated IP address along with its length :", most)
#{'67.218.116.165': 2, '66.249.71.65': 3, '65.55.106.183': 2, '66.249.65.12': 32, '65.55.106.131': 2, '65.55.106.186': 2, '74.52.245.146': 2, '66.249.65.43': 3, '65.55.207.25': 2, '65.55.207.94': 2, '65.55.207.71': 1, '98.242.170.241': 1, '66.249.65.38': 100, '65.55.207.126': 2, '82.34.9.20': 2, '65.55.106.155': 2, '65.55.207.77': 2, '208.80.193.28': 1, '89.248.172.58': 22, '67.195.112.35': 16, '65.55.207.50': 3, '65.55.215.75': 2}
#Most repeated IP address along with its length : ('66.249.65.38', 100)
#*****************************************************************
#Program - 4th
#Wap to print nth line from a file
'''
n = 6
with open (r'D:\PYTHON\Python Class\Day9 30th-31st May\access-log.txt') as file:
    for line_no, line in enumerate(file, start = 1):
        if line_no == n:
            print(line)
            break #already read 6th line so no need to go ahead

'''


#Using is slice
'''
n = 6
from itertools import islice
with open (r'D:\PYTHON\Python Class\Day9 30th-31st May\access-log.txt') as file:
        lines = islice(file, n-1,n)
        print(list(lines))
'''
       
    

#*****************************************************************************************************
