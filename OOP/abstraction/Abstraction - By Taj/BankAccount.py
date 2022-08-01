#


from abc import ABC, abstractmethod

class BankAccount(ABC):
    @abstractmethod
    def deposit(self, amount):
        print("Komal")
        raise Exception
    

    @abstractmethod
    def withdraw(self, amount):
        raise Exception

    @abstractmethod
    def funds_transfer(self, amount):
        raise Exception

    @abstractmethod
    def statement(self):
        raise Exception

class SBI(BankAccount):
    # transaction = []
    # balance = 0
    def deposit(self, amount):
        balance = 0
        balance = balance + amount
        return balance
    
        
    def withdraw(self, amount):
        balance = balance - amount
        return balance

    def funds_transfer(self, to_account, amount):
        to_account.deposit(amount)
        balance -= amount
        return balance

    #def statement(self):
        #pass
        

s1 = SBI()
res = s1.deposit(200)
print(res)


