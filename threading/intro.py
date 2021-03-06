import threading
import time


def sleep_(secs: float) -> None:
    print(f"Sleeping for {secs} secs")
    time.sleep(secs)
    print(f"Sleeping for {secs} is done")


if __name__ == "__main__":

    print("Main")

    thread = threading.Thread(target=sleep_, args=(1.5,))
    thread.start()
    thread.join()

    # Main thread waits for this thread to be completed and
    # then executes the rest of the script when .join() is used

    thread2 = threading.Thread(target=sleep_, args=(5,), daemon=True)
    thread2.start()

    # Daemon Thread is being terminate when the main process is done. It is not waited to be completed

    print("Main done")
