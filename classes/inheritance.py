class Employee:

    raise_amount = 1.04

    def __init__(self, first, last, pay):

        self.first = first
        self.last = last
        self.pay = pay
        self.email = f'{first}.{last}@comp.com'

    def appy_raise(self):
        self.pay = self.pay * self.raise_amount


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)

        self.prog_lang = 'Programming Languages'


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)

        self.employees = [] if employees is None else employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print(f'{emp.first} {emp.last}')


dev = Developer("J.", "Cole", 5000, "Python")
emp = Employee("E.", "Bran", 4500)

mng = Manager("Sue", "Smith", 6000, [dev])

mng.print_emps()
mng.add_emp(emp)
mng.remove_emp(dev)
mng.print_emps()
