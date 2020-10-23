import modified_hr_dataclass
import modified_employees_dataclass
import modified_productivity_dataclass

manager = modified_employees_dataclass.Manager(3000, 1, "Mary Poppins")
secretary = modified_employees_dataclass.Secretary(1500, 2, 'John Smith')
sales_guy = modified_employees_dataclass.SalesPerson(1000, 250, 3, 'Kevin Bacon')
factory_worker = modified_employees_dataclass.FactoryWorker(40, 15, 4, 'Jane Doe')
temporary_secretary = modified_employees_dataclass.TemporarySecretary(40, 9, 5, "Robin Williams")

company_employees = [
    manager,
    secretary,
    sales_guy,
    factory_worker,
    temporary_secretary,
]

productivity_system = modified_productivity_dataclass.ProductivitySystem()
productivity_system.track(company_employees, 40)
payroll_system = modified_hr_dataclass.PayrollSystem()
payroll_system.calculate_payroll(company_employees)