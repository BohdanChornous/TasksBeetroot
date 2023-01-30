import random

# Task 1

lis = [random.randint(-100, 100) for i in range(10)]
min_number = lis[0]

for i in lis:
    if i >= min_number:
        min_number = i

print(*lis)
print(f"Max value is {min_number}, {max(lis)}")

# Task 2

lis_1 = [random.randint(1, 10) for i in range(10)]
lis_2 = [random.randint(1, 10) for i in range(10)]
lis_3 = list(set(([i + j for i, j in zip(lis_1, lis_2)])))

print(lis_3)

# Task 3

lis_4 = list(range(1, 101))
fun = lambda x: x % 7 == 0 and x % 5 != 0
print(*filter(fun, lis_4))