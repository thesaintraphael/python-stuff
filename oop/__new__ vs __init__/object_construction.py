class A:

    def __new__(cls, *args, **kwargs):
        """
        __new__ is the method where object is created
        and should return object

        cls => class A

        Returns:
            created object
        """

        print("new", cls, args, kwargs)
        return super().__new__(cls)

    def __init__(self, *args, **kwargs) -> None:
        """
        __init__ initialize values of object that was created inside __new__ method
        __init__ should not return anything

        self => object of class A

        """
        print("init", self, args, kwargs)


if __name__ == "__main__":

    obj = A(1, 2, 2, x=4)

    # above is equivalent to below, but this can be customized using metaclasses

    # Manually creating obj by calling __new__ first and then initializing values with __init__

    obj = A.__new__(A, 1, 2, 3, x=4)
    if isinstance(obj, A):
        type(obj).__init__(obj, 1, 2, 3, x=4)

    print(obj, "OBJ")
