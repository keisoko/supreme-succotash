from dataclasses import dataclass
@dataclass
class ProductivitySystem:
    def track(self, employees_dataclass, hours):
        print("Tracking Employee Productivity")
        print("==============================")
        for employee in employees_dataclass:
            employee.work(hours)
        print("")