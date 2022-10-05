import functools


def double_nummber(func):
    @functools.wraps(func)
    def wrapper(number: int) -> int:
        number = func(number)
        return number * 2

    return wrapper


@double_nummber
def return_number(number: int) -> int:
    return number


print(return_number(6))
