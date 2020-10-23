from dataclasses import dataclass

@dataclass
class PayrollSystem:
    def calculate_payroll(self, modified_employees_dataclass):
        print("Calculating Payroll")
        print("===================")
        for employee in modified_employees_dataclass:
            print(f"Payroll for: {employee.id} - {employee.name}")
            print(f"- Check amount: {employee.calculate_payroll()}")
            print("")

@dataclass
class SalaryPolicy:
    __slots__ = []
    weekly_salary:int

    def calculate_payroll(self):
        return self.weekly_salary

@dataclass
class HourlyPolicy:
    __slots__ = []
    hours_worked:int
    hour_rate: int
    
    def calculate_payroll(self):
        return self.hours_worked * self.hour_rate

@dataclass
class CommissionPolicy(SalaryPolicy):
    __slots__ = []
    commission: int

    def calculate_payroll(self):
        fixed = super().calculate_payroll()
        return fixed + self.commission
