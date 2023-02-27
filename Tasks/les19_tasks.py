# Task 1

class WithIndex:

    def __init__(self, iterable, start: int = 0):
        self.iterable = iterable
        self.start = start - 1
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        self.start += 1
        if self.index == len(self.iterable):
            raise StopIteration
        return self.start, self.iterable[self.index]


def with_index(iterable, start: int = 0):
    for i in iterable:
        yield start, i
        start += 1


print(*with_index(range(1, 10)))
print(*WithIndex(range(1, 10), 5))


# Task 2

def in_range(start: int, end: int, step: int = 1):
    if step == 0:
        raise ValueError("Step cannot be 0")
    i = start
    if start < end:
        while i <= end:
            yield i
            i += step
    else:
        while i >= end:
            yield i
            i += step


print(*in_range(5, 1, -1))
print(*in_range(2, 10, 2))


# Task 3

class MyIterable:
    def __init__(self, iterable):
        self.iterable = iterable

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index >= len(self.iterable):
            raise StopIteration
        value = self.iterable[self.index]
        self.index += 1
        return value

    def __getitem__(self, index):
        return self.iterable[index]


a = MyIterable(["Hello", "this", "is", "my", "iterable", "object"])

for i in a:
    print(i)
print(a[2])
