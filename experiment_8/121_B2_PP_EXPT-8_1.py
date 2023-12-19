'''class Bank:
    def getroi(self):
        return 10
class SBI:
    def getroi(self):
        return 7
class ICICI:
    def getroi(self):
        return 8
b1 = Bank()
b2 = SBI()
b3 = ICICI()
print("Bank rate of interest: ", b1.getroi())
print("SBI rate of interest: ", b2.getroi())
print("ICICI rate of interest: ", b3.getroi())'''

from abc import ABC, abstractmethod
class Employee(ABC):
    @abstractmethod
    def calculate_salary(self, sal):
        pass
class Developer(Employee):
    def calculate_salary(self, sal):
        finalsalary = sal*1.10
        return finalsalary
emp_1 = Developer()
print(emp_1.calculate_salary(10000))
