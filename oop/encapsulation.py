class Developer:

    def __init__(self, name) -> None:
        self.name = name
        self.__salary = None  # Private obj.__salary will raise an AttributeError
        self._num_bugs_solved = 0
        # Protected. obj._num_bus_solved stil can be accessed, but _ tells that this is an internally used ins

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def get_salary(self, salary):
        self.__salary = salary


dev = Developer("Rafael")
dev.set_salary(3000)
print(dev.get_salary())
