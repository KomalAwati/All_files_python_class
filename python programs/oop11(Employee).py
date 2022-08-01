class Employee:
    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
    
    @property
    def pay(self):
        return self._pay
    
    @pay.setter
    def pay(self, value):
        if not isinstance(value, (int, float)):
            raise Exception("Pay should be a number")
        self._pay = value       # creates an internal variable by "_pay" and assigns value

    @property
    def fname(self):
        return self._fname
    
    @fname.setter
    def fname(self, value):
        if len(value) > 5:
            raise Exception("Fname cannot be more than 5 characters")
        self._fname = value

    def pay_raise(self, percent):
        hike_amount = self.pay * percent
        self.pay = self.pay + hike_amount
