from functools import lru_cache


# maxsize defines the number of calls program going to remember (default=128)
# when typed set to True(default is False) caching will treat 3 and 3.0 as diffenet values
@lru_cache(maxsize=10, typed=False)
def fib(n):

    if n < 2:
        return n
    print(f"calculating fib {n}")
    return fib(n-1) + fib(n-2)


print([fib(num) for num in range(10)])
print(fib.cache_info())
fib.cache_clear()  # Clearing Cache
print(fib.cache_info())
