class Employee:

    raise_amount = 1.04

    def __init__(self, first, last):

        self.first = first
        self.last = last

    @property
    def fullname(self):
        # Now is accesible as emp.fullname. No need to call it
        return f"{self.first} {self.last}"

    @property
    def email(self):
        return f'{self.first}.{self.last}@comp.com'

    @fullname.setter
    def fullname(self, name):
        self.first, self.last = name.split(" ")

    @fullname.deleter
    def fullname(self):
        print("Deleting name")
        self.first, self.last = None, None


emp = Employee("Jermaine", "Cole")

emp.fullname = 'Kendrick Lamar'  # Cant set attriute without setter decorator
print(emp.first, emp.last, emp.fullname, emp.email)


del emp.fullname
print(emp.first, emp.last, emp.fullname, emp.email)
