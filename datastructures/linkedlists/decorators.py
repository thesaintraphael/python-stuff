from functools import wraps


def not_empty(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        llist = args[0]
        if llist.head is None:
            raise ValueError("Operation cannot be performed on empty list")

        return func(*args, **kwargs)

    return wrapper
