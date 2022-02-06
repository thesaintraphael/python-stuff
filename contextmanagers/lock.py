from threading import Lock

lock = Lock()

lock.acquire()
# do_something()

lock.release()  # forgetting may cause deadlock

with lock:
    # do_something()
    pass

# Context managers automatically acquires and releases lock
