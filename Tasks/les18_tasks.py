import re
import functools

# Task 1


class ValidData:

    def __init__(self, email: str):
        self._email = self.validate(email)

    @staticmethod
    def validate(email):
        regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b"
        if re.fullmatch(regex, email):
            return email
        else:
            return False

    @property
    def mail(self):
        return self._email

    @mail.setter
    def mail(self, email):
        self._email = self.validate(email)


mail = ValidData('ab.c@mail.com')
print(mail._email)


# Task 2

class Boss:

    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self._workers = []

    @property
    def boss_workers(self):
        return self._workers

    @property
    def workers(self):
        return self._workers

    def add_worker(self, worker):
        if isinstance(worker, Worker):
            self._workers.append(worker)
        else:
            raise ValueError("Can only add instances of Worker to Boss's workers list!")

    def __str__(self):
        return f"{self.name}, of company: {self.company}"


class Worker:

    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id = id_
        self.name = name
        self.company = company
        self._boss = boss

    @property
    def my_boss(self):
        return self._boss

    @my_boss.setter
    def my_boss(self, new_boss):
        if isinstance(new_boss, Boss):
            self._boss = new_boss
        else:
            raise ValueError("Boss should be an instance of Boss class!")

    def __repr__(self):
        return f"{self.name} work in company {self.company}"


big_boss = Boss(170, "BigBass", "Sony")
other_boss = Boss(170, "LittleBass", "Sony")
creep = Worker(120, "Bob", "Sony", big_boss)
creep2 = Worker(125, "Bob2", "Sony", big_boss)
big_boss.add_worker(creep)
big_boss.add_worker(creep2)

print(creep._boss)
creep.boss = other_boss
print(creep.boss)
print(big_boss._workers)


# Task 3

class TypeDecorators:

    @staticmethod
    def to_type(type_: type):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                value = type_(func(*args, **kwargs))
                return value
            return wrapper
        return decorator

    @staticmethod
    def to_int(func):
        return TypeDecorators.to_type(int)(func)

    @staticmethod
    def to_str(func):
        return TypeDecorators.to_type(str)(func)

    @staticmethod
    def to_bool(func):
        return TypeDecorators.to_type(bool)(func)

    @staticmethod
    def to_float(func):
        return TypeDecorators.to_type(float)(func)


@TypeDecorators.to_int
def do_nothing(string: str):
    return string


print(type(do_nothing('22')))
