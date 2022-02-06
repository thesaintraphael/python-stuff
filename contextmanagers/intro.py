# allows as allocate and release resources


with open("contextmanagers/notes.txt", "w") as file:
    file.write("Helo World")

# same process without context manager
file_ = open("contextmanagers/notes.txt", "w")
try:
    file_.write("Hello")
finally:
    file_.close()
