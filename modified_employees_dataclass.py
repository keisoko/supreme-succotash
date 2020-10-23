from dataclasses import dataclass

from modified_hr_dataclass import (
    SalaryPolicy,
    CommissionPolicy,
    HourlyPolicy
)

from modified_productivity_dataclass import (
    ManagerRole,
    SecretaryRole,
    SalesRole,
    FactoryRole
)

@dataclass 
class Employee:
    __slots__ = ["id", "name"]
    id: int
    name: str

@dataclass
class Manager(Employee, ManagerRole, SalaryPolicy):
    pass

@dataclass
class Secretary(Employee, SecretaryRole, SalaryPolicy):
    pass

@dataclass
class SalesPerson(Employee, SalesRole, CommissionPolicy):
    pass

@dataclass
class FactoryWorker(Employee, FactoryRole, HourlyPolicy):
    pass

@dataclass
class TemporarySecretary(Employee, SecretaryRole, HourlyPolicy):
    pass