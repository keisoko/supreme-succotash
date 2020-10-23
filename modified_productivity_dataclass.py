from dataclasses import dataclass

@dataclass
class ProductivitySystem:
    def track(self, modified_employees_dataclass, hours):
        print("Tracking Employee Productivity")
        print("==============================")
        for employee in modified_employees_dataclass:
            result = employee.work(hours)
            print(f"{employee.name}: {result}")
        print("")

@dataclass
class ManagerRole:
    def work(self, hours):
        return f"screams and yells for {hours} hours"

@dataclass
class SecretaryRole:
    def work(self, hours):
        return f"expends {hours} hours doing office paperwork"

@dataclass
class SalesRole:
    def work(self, hours):
        return f"expends {hours} hours on the phone"

@dataclass
class FactoryRole:
    def work(self, hours):
        return f"manufactures gadgets for {hours} hours"