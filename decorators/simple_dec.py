import functools


def start_end_decorator(func):

    # passing args through decorator
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # before function
        result = func(*args, **kwargs)
        # after function
        return result
    return wrapper


@start_end_decorator
def add_5(num):
    return num + 5


print(add_5(5))  # None if func() is not returned from wrapper
print(help(add_5))  # without functools.wraps it holds informtaion of wrapper
print(add_5.__name__)
