import original_hr_dataclass
import original_employees_dataclass
import original_productivity_dataclass

manager = original_employees_dataclass.Manager(1, "Mary Poppins", 3000)
secretary = original_employees_dataclass.Secretary(2, 'John Smith', 1500)
sales_guy = original_employees_dataclass.SalesPerson(3, 'Kevin Bacon', 1000, 250)
factory_worker = original_employees_dataclass.FactoryWorker(4, 'Jane Doe', 40, 15)

company_employees = [
    manager,
    secretary,
    sales_guy,
    factory_worker
]

productivity_system = original_productivity_dataclass.ProductivitySystem()
productivity_system.track(company_employees, 40)
payroll_system = original_hr_dataclass.PayrollSystem()
payroll_system.calculate_payroll(company_employees)