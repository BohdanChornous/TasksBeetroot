# Task 1
import functools
import time


def decorator_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        value = func(*args, **kwargs)
        end = time.time()
        print(end - start)
        return value
    return wrapper


@decorator_time
def binary_search(lis, search_item):
    low = 0
    high = len(lis) - 1
    middle = (low + high) // 2
    if middle < 0:
        return False
    guess = lis[middle]
    if search_item == guess:
        return True
    return binary_search(lis[:middle], search_item) if guess > search_item else binary_search(lis[middle + 1:], search_item)


lst = list(range(10000000))
val = 999999
print(binary_search(lst, val))


@decorator_time
def fibonacci_series(lis, search_item):
    def fibonacci_generator(n):
        n1 = 0
        n2 = 1
        if n < 1:
            return 0
        elif n == 1:
            return 1
        for _ in range(2, n):
            n1, n2 = n2, (n1 + n2)
        return n2
    m = 0
    while fibonacci_generator(m) < len(lis):
        m += 1
    offset = -1

    while fibonacci_generator(m) > 1:
        i = min(offset + fibonacci_generator(m - 2), len(lis) - 1)  # fibonacci index

        if search_item > lis[i]:
            m -= 1
            offset = i
        elif search_item < lis[i]:
            m -= 2
        else:
            return bool(i)

    if fibonacci_generator(m - 1) and lis[offset + 1] == search_item:
        return bool(offset + 1)
    return False


print(fibonacci_series(lst, val))


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    def __init__(self):
        self._capacity = 50
        self.size = 0
        self.buckets = [None] * self._capacity

    def hash(self, key) -> int:
        hashsum = 0
        # For each character in the key
        for idx, c in enumerate(key):
            # Add (index + length of key) ^ (current char code)
            hashsum += (idx + len(key)) ** ord(c)
            # Perform modulus to keep hashsum in range [0, self.capacity - 1]
            hashsum = hashsum % self._capacity
        return hashsum

    def add(self, key, value):
        # 1. Increment size
        self.size += 1
        # 2. Compute index of key
        index = self.hash(key)
        # Go to the node corresponding to the hash
        node = self.buckets[index]
        # 3. If bucket is empty:
        if node is None:
            # Create node, add it, return
            self.buckets[index] = Node(key, value)
            return
        # 4. Collision! Iterate to the end of the linked list at provided index
        prev = node
        while node is not None:
            prev = node
            node = node.next
        # Add a new node at the end of the list with provided key/value
        prev.next = Node(key, value)

    def find(self, key):
        # 1. Compute hash
        index = self.hash(key)
        # 2. Go to first node in list at bucket
        node = self.buckets[index]
        # 3. Traverse the linked list at this node
        while node is not None and node.key != key:
            node = node.next
        # 4. Now, node is the requested key/value pair or None
        if node is None:
            # Not found
            return None
        else:
            # Found - return the data value
            return node.value

    def remove(self, key):
        # 1. Compute hash
        index = self.hash(key)
        node = self.buckets[index]
        prev = None
        # 2. Iterate to the requested node
        while node is not None and node.key != key:
            prev = node
            node = node.next
        # Now, node is either the requested node or none
        if node is None:
            # 3. Key not found
            return None
        else:
            # 4. The key was found.
            self.size -= 1
            result = node.value
            # Delete this element in linked list
            if prev is None:
                node = None
            else:
                prev.next = prev.next.next
            # Return the deleted language
            return result

    def __len__(self):
        return self.size

    def __contains__(self, item):
        index = self.hash(item)
        # 2. Go to first node in list at bucket
        node = self.buckets[index]
        # 3. Traverse the linked list at this node
        while node is not None and node.key != item:
            node = node.next
        # 4. Now, node is the requested key/value pair or None
        if node is None:
            # Not found
            return False
        else:
            # Found - return the data value
            return True


my_hash = HashTable()
print(len(my_hash))
my_hash.add('a', 'altha')
my_hash.add('b', 'beta')
print(len(my_hash))
print('b' in my_hash)
print(my_hash.find("d"))
