# Task 1

def oops() -> None:
    raise KeyError


def other_function()  -> None:
    try:
        oops()
    except BaseException as err:
        print(type(err))


other_function()

# Task 2


def myfunc(a, b):
    try:
        return int(a)**2 / int(b)
    except (ZeroDivisionError, TypeError) as err:
        return type(err)


print(myfunc(input(), input()))
