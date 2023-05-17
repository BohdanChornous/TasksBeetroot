from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import math
import time
# Task 1


def find_prime(n):
    if n < 0:
        n = -1 * n
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqrt_n = int(math.floor(math.sqrt(n)))
    for j in range(3, sqrt_n + 1, 2):
        if n % j == 0:
            return False
    return True


def thread_pool(numbers):
    with ThreadPoolExecutor() as executor:
        start1 = time.time()
        for number, prime in zip(numbers, executor.map(find_prime, numbers)):
            print(f"{number} is prim {prime}")
        print(f"Time: ProcessPoolExecutor = {time.time() - start1}")


def process_pool(numbers):
    with ProcessPoolExecutor() as executor:
        start2 = time.time()
        for number, prime in zip(numbers, executor.map(find_prime, numbers)):
            print(f"{number} is prim {prime}")
        print(f"Time: ProcessPoolExecutor = {time.time() - start2}")


if __name__ == '__main__':
    numbers_lis = [
        2,  # prime
        1099726899285419,
        1570341764013157,  # prime
        1637027521802551,  # prime
        1880450821379411,  # prime
        1893530391196711,  # prime
        2447109360961063,  # prime
        3,  # prime
        2772290760589219,  # prime
        3033700317376073,  # prime
        4350190374376723,
        4350190491008389,  # prime
        4350190491008390,
        4350222956688319,
        2447120421950803,
        5,  # prime
    ]

    process_pool(numbers_lis)
    thread_pool(numbers_lis)
