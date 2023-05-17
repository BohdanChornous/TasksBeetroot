# Task 1

class MyContext:
    counter = 0

    def __init__(self, name_of: str, mode: str = "r"):
        self.name = name_of
        self.mode = mode
        self.open_file = None

    @classmethod
    def get_count(cls):
        return cls.counter

    def __enter__(self):
        self.open_file = open(self.name, self.mode)
        MyContext.counter += 1
        print(f"Closing context name is {self.name}")
        return self.open_file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.open_file.close()
        print(f"Number of contexts is {self.counter}")
