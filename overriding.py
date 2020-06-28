 
class Employee:
    def __init__(self,name,salary):
        self.nm=name
        self.sal=salary
    def getName(self):
        return self.nm
    def getSalary(self):
        return self.sal

class SalesOfficer(Employee):
    def __init__(self,name,salary,income):
        super().__init__(name,salary)
        self.incnt=income
    def getSalary(self):
        return self.sal+self.incnt

e1=Employee("rajesh",9000)
print("total salary of {} is Rs{}".format(e1.getName(),e1.getSalary()))
e2=SalesOfficer("Kiran",10000,1000)
print("total salary of {} is Rs{}".format(e2.getName(),e2.getSalary()))

