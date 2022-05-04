from abc import ABCMeta, abstractmethod


class IDepartment(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, employees) -> None:
        """implement in subclass"""

    def print_department(self) -> None:
        """implement in subclass"""


class AccountingDepartment(IDepartment):
    def __init__(self, employees) -> None:
        self.employees = employees

    def print_department(self) -> None:
        print(f"Accounting Department {self.employees}")


class DevelopmentDepartment(IDepartment):
    def __init__(self, employees) -> None:
        self.employees = employees

    def print_department(self) -> None:
        print(f"Development Department {self.employees}")


class ParentDepartment(IDepartment):
    def __init__(self, employees) -> None:
        self.employees = employees
        self.base_employees = employees
        self.sub_depts = []

    def add(self, department):
        self.sub_depts.append(department)
        self.employees += department.employees

    def print_department(self) -> None:
        print("Parent Department")
        print(f"Parent Department Base Employees: {self.base_employees}")
        for department in self.sub_depts:
            department.print_department()


dept1 = AccountingDepartment(200)
dept2 = DevelopmentDepartment(200)

parent_dept = ParentDepartment(30)
parent_dept.add(dept1)
parent_dept.add(dept2)

parent_dept.print_department()
