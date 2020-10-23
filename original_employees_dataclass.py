from dataclasses import dataclass

@dataclass
class Employee:    
    __slots__ = ["id", "name"]    
    id: int    
    name: str

@dataclass
class SalaryEmployee(Employee):    
    __slots__ = ["weekly_salary"]    
    weekly_salary: int 
    
    def calculate_payroll(self): 
        return self.weekly_salary

@dataclass
class HourlyEmployee(Employee):    
    __slots__ = ["hours_worked", "hour_rate"]    
    hours_worked: int    
    hour_rate: int 
    
    def calculate_payroll(self): 
        return self.hours_worked * self.hour_rate        

@dataclass
class CommissionEmployee(SalaryEmployee):    
    __slots__ = ["commission"]    
    commission: int
    
    def calculate_payroll(self):        
        fixed = super().calculate_payroll() 
        return fixed + self.commission

@dataclass
class Manager(SalaryEmployee): 
    def work(self, hours): 
        print(f"{self.name} screams and yells for {hours} hours")

@dataclass
class Secretary(SalaryEmployee): 
    def work(self, hours): 
        print(f"{self.name} expends {hours} hours doing office paperwork")

@dataclass
class SalesPerson(CommissionEmployee): 
    def work(self, hours): print(f"{self.name} expends {hours} hours on the phone")

@dataclass
class FactoryWorker(HourlyEmployee): 
    def work(self, hours): print(f"{self.name} manufactures gadgets for {hours} hours")
