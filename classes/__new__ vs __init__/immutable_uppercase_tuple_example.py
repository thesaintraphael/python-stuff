class UppercaseTuple(tuple):

    def __new__(cls, iterable):
        upper_iterable = (element.upper() for element in iterable)
        return super().__new__(cls, upper_iterable)

    # Error: tuples are immutable, even in init
    # def __init__(self, iterable):
    #     print(f'init {iterable}')
    #     for i, arg in enumerate(iterable):
    #         self[i] = arg.upper()


if __name__ == "__main__":

    print("UPPERCASE TUPLE EXAMPLE")
    print(UppercaseTuple(["hi", "there"]))
