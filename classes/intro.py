import datetime


class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):

        self.first = first
        self.last = last
        self.pay = pay
        self.email = f'{first}.{last}@comp.com'

        Employee.num_of_emps += 1

    def appy_raise(self):
        # Employee.raise_amount is also accesible
        self.pay = self.pay * self.raise_amount

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        return day.weekday() not in [5, 6]


emp_1 = Employee("Jon", "Snow", 2500)
emp_2 = Employee("Rob", "Stark", 3500)


date = datetime.date(2022, 2, 26)
print(Employee.is_workday(date))


# emp_str_1 = "John-Doe-70000"
# new_emp1 = Employee.from_string(emp_str_1)
# print(new_emp1, "New Employee")

# Employee.set_raise_amount(1.6)  # calling with instance also possible

# print(Employee.raise_amount)  # 1.6
# print(emp_2.raise_amount)  # 1.6


# emp_1.raise_amount = 1.05  # changes raise amount variable only for this object

# print("raise_amount" in emp_1.__dict__)  # True
# print("raise_amount" in emp_2.__dict__)  # False but still accesible


# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)


# print(f"Number of employees {Employee.num_of_emps}")
