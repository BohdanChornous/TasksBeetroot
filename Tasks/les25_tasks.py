# Task 1

class Node:
    def __init__(self, data_val=None):
        self.data_val = data_val
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def add_to_end(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def del_from_end(self):
        if self.head is None:
            return None
        if self.head.next is None:
            self.head = None
            return None
        prev = self.head
        current = self.head.next
        while current.next:
            prev = current
            current = current.next
        prev.next = None
        return current.data_val

    def search(self, val):
        current = self.head
        while True:
            if current.dataval == val:
                return current.dataval
            if current.next is None:
                break
            current = current.next
        return None

    def stak_print(self):
        print_val = self.head
        while print_val is not None:
            print(print_val.data_val, "-> ", end="")
            print_val = print_val.next
        print()


class Queue:
    def __init__(self):
        self.head = None

    def add_to_front(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        self.head, self.head.next = new_node, self.head

    def add_to_end(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def del_from_front(self):
        current = self.head
        if self.head is None:
            return None
        self.head = self.head.next
        return current.data_val

    def del_from_end(self):
        if self.head is None:
            return None
        if self.head.next is None:
            self.head = None
            return None
        prev = self.head
        current = self.head.next
        while current.next:
            prev = current
            current = current.next
        prev.next = None
        return current.data_val

    def insert(self, val, pos=0):
        if pos == 0:
            self.add_to_front(val)
            return
        if pos >= self.len_q():
            self.add_to_end(val)
            return
        new_node = Node(val)
        counter = 0
        prev = self.head
        current = self.head.next
        while True:
            counter += 1
            if counter == pos:
                prev.next, new_node.next = new_node, current
                break
            prev = current
            current = current.next

    def remove(self, val):
        new_node = Node(val)
        if new_node.data_val == self.head.data_val:
            self.del_from_front()
            return
        prev = self.head
        current = self.head.next
        while current:
            if new_node.data_val == current.data_val:
                prev.next = current.next
                break
            prev = current
            current = current.next

    def search(self, val):
        current = self.head
        while True:
            if current.data_val == val:
                return current.data_val
            if current.next is None:
                break
            current = current.next
        return None

    def len_q(self):
        counter = 0
        current = self.head
        while current:
            counter += 1
            current = current.next
        return counter

    def queue_print(self):
        print_val = self.head
        while print_val is not None:
            print(print_val.data_val, "-> ", end="")
            print_val = print_val.next
        print()

