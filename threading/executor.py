import concurrent.futures
import time


def sleep_(secs: float) -> str:
    print(f"Sleeping for {secs} secs.")
    time.sleep(secs)
    return f"Slept for {secs} secs."


with concurrent.futures.ThreadPoolExecutor() as executor:

    """Submit returns future object that allows us to check the status of the process, access result of it"""

    f1 = executor.submit(sleep_, 2)  # passing in function and args
    print(f"Result: {f1.result()}")  # kind of "waiting around" and gettig the result


with concurrent.futures.ThreadPoolExecutor() as executor:

    """Using map instead of list comprehension

    NOTE: passing arguments to non argument function here can cause "silent"
        error that may debugging proccess harder

    """

    seconds = [5, 4, 3, 2, 1]

    results = executor.map(sleep_, seconds)

    for result in results:
        print(result)
