#


from abc import ABC, abstractclassmethod, abstractmethod

class BankAccount(ABC):
    @abstractmethod
    def deposit(self, amount):
        self.amount = amount
        amount = 200
        # raise Exception


class SBI(BankAccount):
    # transaction = []
    # balance = 0
    def deposit(self, amount):
        balance = 0
        balance = balance + amount
        return balance
        
        

s1 = SBI()
res = s1.deposit(200)
print(res)

