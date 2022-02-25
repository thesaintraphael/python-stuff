class Employee:

    def __init__(self, first, last, pay) -> None:

        self.first = first
        self.last = last
        self.pay = pay
        self.email = f'{first}.{last}@comp.com'


emp = Employee("Jon", "Snow", 2500)
