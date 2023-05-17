# Task 1
import multiprocessing
import time

def fibonacci(number: int):
    first, second = 0, 1
    if number < 0:
        print("Incorrect input")
    elif number == 0:
        print(f"fibonacci 0")
    elif number == 1 or number == 2:
        print(f"fibonacci 1")
    else:
        for i in range(number):
            first, second = second, first + second
        print(f"fibonacci {first}")
def factorial(number: int):
    ans = 1
    if number < 0:
        print("Incorrect input")
    elif number == 0:
        print(f"factorial 0")
    elif number == 1:
        print(f"factorial 1")
    else:
        for i in range(2, number + 1):
            ans *= i
        print(f"factorial {ans}")

def squares(number: int):
    print(f'squares {pow(number, 2)}')

def cubes(number: int):
    print(f'cubic {pow(number, 3)}')

def calculate_all(n):
    fib = fibonacci(n)
    fact = factorial(n)
    sqr = squares(n)
    cub = cubes(n)

def main():
    pool = multiprocessing.Pool()
    pool.map(calculate_all, range(10))

if __name__ == '__main__':
    start = time.time()
    main()
    print(time.time() - start)
