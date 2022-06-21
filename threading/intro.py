import threading
import time


def sleep_(secs: float) -> None:
    print(f"Sleeping for {secs} secs")
    time.sleep(secs)
    print(f"Sleeping for {secs} is done")


if __name__ == "__main__":

    print("Main")

    threading.Thread(target=sleep_, args=(1.5,)).start()

    print("Main done")
