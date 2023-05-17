import functools
import re

# Task 1


def logger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        value = func(*args, **kwargs)
        print(func.__name__, "called with", *args)
        return value
    return wrapper


@logger
def add(x, y):
    return x + y


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]


print(add(3, 4))


# Task 2


def stop_words(words: list):
    def decorator(func):
        def wrapper(*args, **kwargs):
            value = func(*args, **kwargs)
            print(value)
            my_value = re.sub("|".join(words), "*", value)
            return my_value
        return wrapper
    return decorator


@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


print(create_slogan("Bohdan"))


# Task 3


def arg_rules(type_: type, max_length: int, contains: list):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for arg in args:
                if not isinstance(arg, type_):
                    print(f"Argument {arg} is not of type {type_}")
                    return False
                if len(str(arg)) > max_length:
                    print(f"Argument {arg} exceeds the maximum length of {max_length}")
                    return False
                if any(symbol not in str(arg) for symbol in contains):
                    print(f"Argument {arg} does not contain all the required symbols: {contains}")
                    return False
            return func(*args, **kwargs)
        return wrapper
    return decorator


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"
