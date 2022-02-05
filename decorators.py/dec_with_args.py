import functools


def repeat(times=1):

    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper

    return decorator_repeat


@repeat(times=3)
def greet(name):
    print(f'Hello, {name}')


greet("Alex")
