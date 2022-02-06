from contextlib import contextmanager


@contextmanager
def open_managed_file(file_name):
    file = open(file_name, "w")
    try:
        yield file
    finally:
        file.close()


with open_managed_file("contextmanagers/notes.txt") as file_:
    file_.write("Hello...")
