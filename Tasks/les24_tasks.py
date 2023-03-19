import sys
from collections import deque


# Task 1


lst_in = list(map(str.strip, sys.stdin.readlines()))

st = deque()
st.extendleft(lst_in)
print(st)


# Task 2

def is_correct_bracket(text):
    counter = 0
    for c in text:
        if c == '(':
            counter += 1
        else:
            counter -= 1
        if counter < 0:
            break
    return counter == 0


# Task 3


class Stack:
    def __init__(self):
        self._items = []

    def is_empty(self):
        return bool(self._items)

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def peek(self):
        return self._items[len(self._items) - 1]

    def size(self):
        return len(self._items)

    def get_from_stack(self, elem):
        for e in self._items:
            if e == elem:
                return elem
        raise ValueError

    def __repr__(self):
        representation = "<Stack>\n"
        for ind, item in enumerate(reversed(self._items), 1):
            representation += f"{ind}: {str(item)}\n"
        return representation

    def __str__(self):
        return self.__repr__()


class Queue:
    def __init__(self):
        self._items = []

    def is_empty(self):
        return bool(self._items)

    def enqueue(self, item):
        self._items.insert(0, item)

    def dequeue(self):
        return self._items.pop()

    def size(self):
        return len(self._items)

    def get_from_stack(self, elem):
        for e in self._items:
            if e == elem:
                return elem
        raise ValueError

    def __repr__(self):
        representation = "<Queue>\n"
        for ind, item in enumerate(reversed(self._items), 1):
            representation += f"{ind}: {str(item)}\n"
        return representation

    def __str__(self):
        return self.__repr__()
