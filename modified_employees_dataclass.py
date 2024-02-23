"""HR Employees classes"""

from dataclasses import dataclass

from modified_hr_dataclass import SalaryPolicy, CommissionPolicy, HourlyPolicy

from modified_productivity_dataclass import (
    ManagerRole,
    SecretaryRole,
    SalesRole,
    FactoryRole,
)


@dataclass
class Employee:
    """Employee class"""

    __slots__ = ["id", "name"]
    id: int
    name: str


@dataclass
class Manager(Employee, ManagerRole, SalaryPolicy):
    """Manager class"""


@dataclass
class Secretary(Employee, SecretaryRole, SalaryPolicy):
    """Secretary class"""


@dataclass
class SalesPerson(Employee, SalesRole, CommissionPolicy):
    """Sales person class"""


@dataclass
class FactoryWorker(Employee, FactoryRole, HourlyPolicy):
    """Factory worker class"""


@dataclass
class TemporarySecretary(Employee, SecretaryRole, HourlyPolicy):
    """Temporary Secretary class"""
