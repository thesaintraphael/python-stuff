class Employee:

    raise_amount = 1.04

    def __init__(self, first, last, pay):

        self.first = first
        self.last = last
        self.pay = pay
        self.email = f'{first}.{last}@comp.com'

    def appy_raise(self):
        self.pay = self.pay * self.raise_amount

    def __str__(self) -> str:
        return f'{self.email}'

    def __repr__(self) -> str:
        return f'Employee({self.first}, {self.last}, {self.pay})'

    def __add__(self, other):
        # Ovveriding + operator
        return self.pay + other.pay

    def __lt__(self, other):
        # comparing objects. Now we can sort list of EMPs
        return self.pay < other.pay

    def __len__(self):
        # implementation: len(emp)
        return len(self.first)

    # def __getitem__(self, key):
        # overriding emp[i]

    # def __contains__(self, value):
        # overriding in operator

    # def __iadd__(self, other):
        # imp: self.instance += other.instance

    '''
        Other operators
        __sub__(self, other) (-)
        __isub__(self, other) (-=)
        __mul__(self, other) (*)
        __imul__(self, other) (*=)
        __truediv__(self, other) (\)
        __itruediv__(self, other) (\=)
        __floordiv__(self, other) (\\)
    '''

    def __call__(self, *args, **kwds):
        # imp: emp.call()
        print("Employee is called")


emp_1 = Employee("Anna", "Jean", 3500)

print(emp_1)  # calling __str__ method (aslo when doing str(emp_1))
repr(emp_1)  # calling __repr__ method
