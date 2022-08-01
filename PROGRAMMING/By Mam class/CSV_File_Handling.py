#Write a program to read all the names  of the employees in employee.csv file
import csv
path = r"D:\PYTHON\Python Class\Day11 2nd Jan\employees.csv"
''' 

# reader()

with open(path) as file:
    rows = csv.reader(file)
    header = next(rows)
    for r in rows:
        print(r[0])

   
# DictReader()
with open(path) as file:
    rows = csv.DictReader(file)
    for name in rows:
        print(name)   
'''

     
# Write a program to print only the salaries that are > 70000

'''
# reader()
with open(path) as file:
    rows = csv.reader(file)
    header = next(rows)
    for info in rows:
        if int(info[2]) > 7000:
            print(info[2])
            
#DictReader
with open(path) as f:
    rows = csv.DictReader(f)
    header = next(rows)
    for r1 in rows:
        if r1['pay'] > '7000':
            print(r1['pay'])
'''

#Write a program to group male and female employee in the file

gender1  = {}
with open (path) as f:
    rows = csv.DictReader(f)
    for row in rows:
        if row['gender'] not in gender1:
            gender1[gender] = ["fname"]
        else:
            gender1[gender].append('fname')
                
'''  
#WAP to group an employees to based on their team

d = {}
with open(path) as file:
    rows= csv.reader(file)
    header = next(rows)
    for i in rows:
        if i[2] not in d:
            d[i[2]]== d[i[0]]
        else:
            d[i[2]].append(d[])
'''
    
        
              
