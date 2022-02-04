from functools import wraps


def mylogger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Running {func.__name__}")
        return func(*args, **kwargs)
    return wrapper


@mylogger
def add(a, b):
    """adds a and b"""
    return a + b


# add(1, 2)
print(add.__name__)  # will wrapper if we dont use @wraps
print(add.__doc__)  # will None if we dont use @wraps
