from functools import total_ordering


@total_ordering
class Car:
    def __init__(self, model, mileage):
        self.model = model
        self.mileage = mileage

    def __eq__(self, other):
        return self.mileage == other.mileage

    def __lt__(self, other):
        return self.mileage <= other.mileage


car1 = Car("Audi", 800)
car2 = Car("BMV", 800)

print(car1 == car2)
# Nomrally it will throw an error,
# but total_ordering using the __lt__ function
# and generate other comparison funtions based on lt comp logic


# NOTE: total_ordering may slow down code execution
