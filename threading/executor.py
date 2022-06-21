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


# TPE with loops

with concurrent.futures.ThreadPoolExecutor() as executor:

    seconds = [5, 4, 3, 2, 1]

    future_objects = [executor.submit(sleep_, sec) for sec in seconds]

    for future_object in concurrent.futures.as_completed(future_objects):
        # Printing out result of each proccess when it is completed
        print(future_object.result())
