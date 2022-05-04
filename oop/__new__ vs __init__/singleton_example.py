class Singleton:

    _instance = None

    # There should be ony one object of Singleton class

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)

        return cls._instance


if __name__ == "__main__":

    obj_1 = Singleton()
    obj_2 = Singleton()  # does not creating new object, instead returning previous

    print(f"{obj_1 is obj_2 = }")
