from typing import Callable


class CountCalls:
    def __init__(self, func: Callable) -> None:
        self.func = func
        self.times_called = 0

    def __call__(self, *args, **kwargs):
        self.times_called += 1
        print(f"Called {self.times_called} times")
        return self.func(*args, **kwargs)


@CountCalls
def say_hello():
    print("Hello")


say_hello()
say_hello()
say_hello()
