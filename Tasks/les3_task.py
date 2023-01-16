# Task 1

input_strint = input("Enter string: ")

if len(input_strint) > 2:
    print(input_strint[:2] + input_strint[-2:])
elif len(input_strint) == 2:
    print(input_strint * 2)
else:
    print("Empty String")

# Task 2

phone_number = input("Enter phone number: ")

if phone_number.isdigit() and len(phone_number) == 10:
    print('Phone number is correct')
else:
    print('Wrong phone number')

print(True if phone_number.isdigit() and len(phone_number) == 10 else False)

# Task 3

math_expr = int(input("Enter your answer 2 * 2: "))

while math_expr != 4:
    math_expr = int(input("wrong answer try again 2 * 2: "))
print("Its correct answer")

# Task 4

my_name = "bohdan"

name = input("Enter your name: ")

while name != my_name or name != my_name.title():
    name = input("You enter wrong name try again: ")
print(True)

# if name == my_name or name == my_name.title():
#     print(True)
# else:
#     print(False)

# Task form classroom

month = int(input("Введыть мысяць народження: "))

if month == 1 or 2 or 12:
    print("Ви народилися взимку")
elif month == 3 or 4 or 5:
    print("Ви народилися восени")
elif month == 6 or 7 or 8:
    print("Ви народилися влітку")
elif month == 9 or 10 or 11:
    print("Ви народилися осінню")
else:
    print("Такого місяця ще не вигадали")
