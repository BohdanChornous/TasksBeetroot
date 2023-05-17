# Task 1
import asyncio
import time

async def fibonacci(number: int):
    first, second = 0, 1
    if number < 0:
        #await asyncio.sleep(0.2)
        print("Incorrect input")
    elif number == 0:
        #await asyncio.sleep(0.2)
        print(f"fibonacci 0")
    elif number == 1 or number == 2:
        #await asyncio.sleep(0.2)
        print(f"fibonacci 1")
    else:
        for i in range(number):
            first, second = second, first + second
        #await asyncio.sleep(0.2)
        print(f"fibonacci {first}")

async def factorial(number: int):
    ans = 1
    if number < 0:
        #await asyncio.sleep(0.2)
        print("Incorrect input")
    elif number == 0:
        #await asyncio.sleep(0.2)
        print(f"factorial 0")
    elif number == 1:
        #await asyncio.sleep(0.2)
        print(f"factorial 1")
    else:
        for i in range(2, number + 1):
            ans *= i
        #await asyncio.sleep(0.2)
        print(f"factorial {ans}")

async def squares(number: int):
    #await asyncio.sleep(0.2)
    print(f'squares {pow(number, 2)}')

async def cubic(number: int):
    #await asyncio.sleep(0.2)
    print(f'cubic {pow(number, 3)}')

async def gather_tasks():
    for i in range(10):
        await asyncio.gather(
            fibonacci(i),
            factorial(i),
            squares(i),
            cubic(i),
        )


if __name__ == '__main__':
    start = time.time()
    asyncio.run(gather_tasks())
    print(time.time() - start)

