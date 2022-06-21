import threading
import time
from intro import sleep_


if __name__ == "__main__":

    start = time.perf_counter()
    print("Main start")

    threads = []

    for _ in range(10):
        thread = threading.Thread(target=sleep_, args=(2,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()
        # joining to calculate whole execution time

    end = time.perf_counter()

    print("Main end")

    print(f"{round(end - start, 2)} secs")
