# Task 1

def favorite_movie(film: str) -> None:
    print(f"My favorite movie is named {film}")


favorite_movie(input("Enter your favorite movie "))

# Task 2


def make_country(country: str, cap: str) -> None:
    dict_capitals = {}
    dict_capitals[country] = dict_capitals.get(country, cap)
    print(dict_capitals)


name, capital = input(), input()

make_country(name, capital)


def make_operation(operator: str, numbers: list) -> int:
    if operator == '+':
        result = 0
        for i in numbers:
            result += i
        return result
    elif operator == '-':
        result = 0
        for i in numbers:
            result -= i
        return result
    elif operator == '*':
        result = 1
        for i in numbers:
            result *= i
        return result


operation = input()
num = [int(input("Enter number: ")) for i in range(int(input("Enter quantity of numbers ")))]

print(make_operation(operation, num))
