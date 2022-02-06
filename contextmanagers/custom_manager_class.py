class ManagedFile:

    def __init__(self, file_name) -> None:
        self.file_name = file_name

    def __enter__(self):
        
        self.file = open(self.file_name, "w")
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.file:
            self.file.close()
            

with ManagedFile("contextmanagers/notes.txt") as file:
    file.write("Hello World")