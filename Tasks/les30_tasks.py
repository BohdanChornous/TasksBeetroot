import threading
# Task 1


class Counter(threading.Thread):
    counter = 0
    randon = 100000

    def run(self):
        for i in range(self.randon):
            self.counter += 1


tr1 = Counter()
tr2 = Counter()

tr1.start()
tr2.start()

tr1.join()
tr2.join()

print(tr1.counter + tr2.counter)
