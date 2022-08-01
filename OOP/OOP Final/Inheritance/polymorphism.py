class Employee():
    _minsalary = 12000
    _maxsalary = 50000
    _companyname = 'ABC'
    def __init__(self,name,salary,department):
        self._name = name  
        self._salary = salary
        self._department = department
    def _showData(self):
        print('Employee name: ' + self.getName() + '\n' +
              'salary: ' + self.getSalary())
    def getName(self):
        return self._name
    def getSalary(self):
        return str(self._salary)
#class child
class Accounting(Employee):
    __departmentName = 'Accounting Department'
    def __init__(self,name,salary,age):
        super().__init__(name,salary,self.__departmentName)
        self.age = age
    def _showData(self):
        super()._showData()
        print('age: ' + str(self.age))
        
class Sale(Employee):
    __departmentName = 'Sales Department'
    def __init__(self,name,salary,area):
        super().__init__(name,salary,s1.__departmentName)
        self.area = area
    def _showData(self):
        super()._showData()
        print('Work area: ' + self.area)
            
account = Accounting('Eda',40000,30)
account._showData()
sale = Sale('Fiffy',35000,'CNX')
sale._showData()
