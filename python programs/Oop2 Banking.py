#************************************************************************
#Program -1st:
#Deposit
'''
class BankAccount:
    # shared by all the customers or instances of BankAccount class
    interest_rate = 0.05    # class variable
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        self.transactions = [ ]
        self.transactions.append(f"**** Inital deposit : {balance} ***********")
    
    def deposit(self, amount):
        self.balance = self.balance + amount
        self.transactions.append(f"Amount deposited: {amount}")

c1 = BankAccount("steve", 1000)
c2 = BankAccount("bill", 2000)
c3 = BankAccount("Amy", 3000)
c4 = BankAccount("Alex")
'''

#O/p -
#c1.deposit(1000)
#c1.__dict__
#{'name': 'steve', 'balance': 2000, 'transactions': ['**** Inital deposit : 1000 ***********', 'Amount deposited: 1000']}

#*************************************************************************
#Program -1st:(Practice)
#deposit
'''
class BankAccount:
    def __init__(self,name,balance = 0):
        self.name = name
        self.balance = balance
        self.transactions = []
        self.transactions.append(f"****** Initial Deposit : {balance} ***********")
    def deposit(self, amount):
        self.balance = self.balance + amount
        self.transactions.append(f"******** Amount Deposited : {amount} ****************")
c1 = BankAccount('Komal', 1000)
c2 = BankAccount("Bmw", 2000)
c3 = BankAccount("Neeta", 3000)

c1.deposit(100)
print(c1.__dict__)
print(c1.balance)'''

#O/p-
{'name': 'Komal', 'balance': 1100, 'transactions': ['****** Initial Deposit : 1000 ***********', '******** Amount Deposited : 100 ****************']}
#1100

#*************************************************************************
#Program - 2nd
#Withdraw
'''
class BankAccount:
    def __init__(self,name,balance = 0):
        self.name = name
        self.balance = balance
        self.transactions = []
        self.transactions.append(f"****** Initial amount : {balance} ***********")
    def withdraw(self,amount):
    if amount > self.balance:
            raise Exception("Insufficient Funds")
        self.balance = self.balance - amount
        self.transactions.append(f"******** Withdraw Amount : {amount}")


c1 = BankAccount('Komal', 1000)
c2 = BankAccount("Bmw", 2000)
c3 = BankAccount("Neeta", 3000)

c2.withdraw(200)
print(c2.__dict__)
'''

#O/p-
#{'name': 'Bmw', 'balance': 1800, 'transactions': ['****** Initial amount : 2000 ***********', '******** Withdraw Amount : 200']}


#**************************************************************************
#Program - 3rd
#Statements
'''
class BankAccount:
    # shared by all the customers or instances of BankAccount class
    interest_rate = 0.05    # class variable
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        self.transactions = [ ]
        self.transactions.append(f"**** Inital deposit : {balance} ***********")
    
    def deposit(self, amount):
        self.balance = self.balance + amount
        self.transactions.append(f"Amount deposited: {amount}")
    
    def withdraw(self, amount):
        if amount > self.balance:
            raise Exception("Insufficient Funds")
        self.balance = self.balance - amount
        self.transactions.append(f"Amount withdrawn: {amount}")
    
    def statement(self):
        for item in self.transactions:
            print(item)
        print(f"*********** Total Balance {self.balance} ************* ")
    
c1 = BankAccount("steve", 1000)
c2 = BankAccount("bill", 2000)
c3 = BankAccount("Amy", 3000)
c4 = BankAccount("Alex")

c2.deposit(200)
c2.withdraw(100)
c2.statement()
'''
#O/p-
'''
**** Inital deposit : 2000 ***********
Amount deposited: 200
Amount withdrawn: 100
*********** Total Balance 2100 *************
'''
#**************************************************************************
#Program - 4th
#Transfer funds

'''

class BankAccount:
    # shared by all the customers or instances of BankAccount class
    interest_rate = 0.05    # class variable
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        self.transactions = [ ]
        self.transactions.append(f"**** Inital deposit : {balance} ***********")
        
    def deposit(self, amount):
        self.balance = self.balance + amount
        self.transactions.append(f"Amount deposited: {amount}")
    
    
    def transfer_funds(self, to_account, amount):
        if amount > self.balance:
            raise Exception("Insufficent Funds!!!")
        to_account.deposit(amount)
        self.balance = self.balance-amount

    
c1 = BankAccount("steve", 1000)
c2 = BankAccount("bill", 2000)
c3 = BankAccount("Amy", 3000)
c4 = BankAccount("Alex")

c1.transfer_funds(c2, 100)
print(c2.__dict__)

'''
#O/p-
#{'name': 'bill', 'balance': 2100, 'transactions': ['**** Inital deposit : 2000 ***********', 'Amount deposited: 100']}

#print(c1.__dict__)


{'name': 'steve', 'balance': 900, 'transactions': ['**** Inital deposit : 1000 ***********']}

#***********************************************************************************************************************       
#Program - 8th
#Rate Of Interest

class BankAccount:
    # shared by all the customers or instances of BankAccount class
    interest_rate = 0.05    # class variable
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        self.transactions = [ ]
        self.transactions.append(f"**** Inital deposit : {balance} ***********")
        
class Bank:
    # shared by all the customers or instances of BankAccount class
    interest_rate = 0.05    # class variable
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        self.transactions = [ ]
        self.transactions.append(f"**** Inital deposit : {balance} ***********")
    def roi(self):
        int_amount = self.balance * Bank.interest_rate
        self.balance = self.balance + int_amount

c1 = Bank("steve", 1000)
c2 = Bank("bill", 2000)
c3 = Bank("Amy", 3000)
c4 = Bank("Alex")

c1.roi()
print(c1.__dict__)

#O/p -
{'name': 'steve', 'balance': 1050.0, 'transactions': ['**** Inital deposit : 1000 ***********']}
 



