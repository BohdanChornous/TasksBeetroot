# Task 1

import random

random_number = random.randint(1, 10)
my_number = int(input("Try to guess number from 1 to 10: "))

if my_number == random_number:
    print("Congratulations, you guessed the number")
else:
    print("You didn't guess")

# Task 2

name = input("Enter your name: ")
age = int(input("Enter your current age"))

print(f"Hello {name}, on your next birthday you’ll be {age + 1} years")

# Task 3

your_string = input()
counter = 0
new_string = ""

while counter < 5:
    counter += 1
    rand_string = random.randint(0, len(your_string) - 1)
    new_string += your_string[rand_string]
print(new_string)
