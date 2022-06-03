from functools import cached_property


class Marksheet:
    def __init__(self, *grades):
        self.grades = grades

    @cached_property
    def total(self):
        print("Calculating total.")
        return sum(self.grades)

    @cached_property
    def average(self):
        print("Calculating average.")
        return self.total / len(self.grades)


m = Marksheet(100, 90, 95)
print(m.total)
print(m.average)
# We dont see Calculating total text again,
# because it doesn not running again thanks to cashed_property function

# Same happens when we call average for second time.
# No calculating average text
print(m.average)
