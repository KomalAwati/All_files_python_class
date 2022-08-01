from csv import reader, DictReader
def read_csv():
    with open("D:\PYTHON\Python Class\Day11 2nd Jan\employees.csv") as f:
        records = []
        rows = DictReader(f)
        for row in rows:
            records.append(row)
    return records
print("read_csv :\n", read_csv())

# i want to know the total pay that i am paying to all the employees as salary
def total_pay():
    data = read_csv()
    total = 0.00
    for item in data:
        total = total + float(item['pay'])
    return total
print("total_pay :\n", total_pay())

# by_gender = {"Male": 6, "Female": 5}
def total_count_by_gender():
    data = read_csv()
    by_gender = {}
    for item in data:
        gender = item['gender']
        if gender in by_gender:
            by_gender[gender]=by_gender[gender] + 1
        else:
            by_gender[gender]= 1
    return by_gender
print("total_count_by_gender : \n", total_count_by_gender())

#highest_pay()
def highest_pay():
    data = read_csv()
    by_pay = sorted(data, key=lambda item: float(item['pay']))
    return by_pay
print("highest_pay : \n" , highest_pay())

#O/p - (It wil just sort according to the pay in the ascending order)
#highest_pay : 
#[{'fname': 'laura', 'lname': 'turner', 'pay': '2000', 'gender': 'female', 'team': 'marketing'}, {'fname': 'milinda', 'lname': 'gates', 'pay': '2500', 'gender': 'female', 'team': 'testing'}, {'fname': 'sara', 'lname': 'joseph', 'pay': '2800', 'gender': 'female', 'team': 'testing'}, {'fname': 'john', 'lname': 'doe', 'pay': '3500', 'gender': 'male', 'team': 'testing'}, {'fname': 'steve', 'lname': 'jobs', 'pay': '4000', 'gender': 'male', 'team': 'development'}, {'fname': 'steve', 'lname': 'wozniak', 'pay': '4500', 'gender': 'male', 'team': 'marketing'}, {'fname': 'johny', 'lname': 'ive', 'pay': '4900', 'gender': 'male', 'team': 'development'}, {'fname': 'bill', 'lname': 'gates', 'pay': '5000', 'gender': 'male', 'team': 'development'}, {'fname': 'tim', 'lname': 'cook', 'pay': '6000', 'gender': 'male', 'team': 'marketing'}, {'fname': 'guido', 'lname': 'rossum', 'pay': '8000', 'gender': 'male', 'team': 'development'}]
'''
for item in data:
    print(item)

top_3 = item[-3:]
least_3 = item[:3]
print("top_3 :", top_3)
print("least_3 :", least_3)
'''

#Fecth the unique teams name


        
        
    
    
