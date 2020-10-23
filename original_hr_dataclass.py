from dataclasses import dataclass
@dataclass
class PayrollSystem:
    def calculate_payroll(self, employees_dataclass):
        print("Calculating Payroll")
        print("===================")
        for employee in employees_dataclass:
            print(f'Payroll for: {employee.id} - {employee.name}')
            print(f'- Check amount: {employee.calculate_payroll()}')
            print("")