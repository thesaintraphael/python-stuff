import functools


def double_number(func):
    @functools.wraps(func)
    def wrapper(number: int) -> int:
        number = func(number)
        return number * 2

    return wrapper


@double_number
def return_number(number: int) -> int:
    return number


print(return_number(6))
