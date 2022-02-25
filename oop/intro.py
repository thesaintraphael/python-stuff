# Classes, Instances and Class variables


class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay) -> None:

        self.first = first
        self.last = last
        self.pay = pay
        self.email = f'{first}.{last}@comp.com'

        Employee.num_of_emps += 1

    def appy_raise(self):
        # Employee.raise_amount is also accesible
        self.pay = self.pay * self.raise_amount


emp_1 = Employee("Jon", "Snow", 2500)
emp_2 = Employee("Rob", "Stark", 3500)

emp_1.raise_amount = 1.05  # changes raise amount variable only for this object

print("raise_amount" in emp_1.__dict__)  # True
print("raise_amount" in emp_2.__dict__)  # False but still accesible


print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)


print(f"Number of employees {Employee.num_of_emps}")
