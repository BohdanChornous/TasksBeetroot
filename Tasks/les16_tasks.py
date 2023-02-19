# Task 4


class CustomException(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        with open('logs.txt', 'a') as file:
            file.write(f'{msg}\n')


# Task 1

class Person:

    def __init__(self, name: str, surname: str, age: int):
        self.name = name
        self.surname = surname
        self.age = age

    def introduce(self):
        print(f"Hi I'm {self.name} my full name is {self.name} {self.surname}. I am {self.age} years old.")

    def __str__(self):
        return f"{self.name} {self.surname}"


class Student(Person):

    def __init__(self, name: str, surname: str, age: int):
        super().__init__(name, surname, age)
        self.subjects = set()

    def add_subject(self, new_subject: str):
        self.subjects.add(new_subject)
        print(f"{str(self)} enroll in a subject {new_subject}")

    def quit_subject(self, name_subject: str):
        if name_subject in self.subjects:
            self.subjects.remove(name_subject)
            print(f"{str(self)} quit subject {name_subject}")
        else:
            print(f"{str(self)} not enroll in {name_subject}")


class Teacher(Person):

    def __init__(self, name: str, surname: str, age: int, salary: int, subject: str):
        super().__init__(name, surname, age)
        self.salary = salary
        self.subject = subject
        self.les_schedule = {}

    def schedule(self, week_day: str, time: str):
        self.les_schedule.setdefault(week_day, []).append(time)

    def check_schedule(self):
        for k, v in self.les_schedule.items():
            print(f"{self.subject}: {k}")
            for t in v:
                print(t)

    def check_day(self, day_week: str):
        if day_week in self.les_schedule.keys():
            print(f"{self.subject}: {day_week}")
            print(*self.les_schedule[day_week], sep="\n")
        else:
            print(f"{str(self)} dont have any lesson in {day_week}")

    def check_salary(self):
        print(f"{str(self)} salary is {self.salary}")


magic_teacher = Teacher("Gandalf", "Gray", 5000, 10000, "fiery magic")
magic_teacher.introduce()
magic_teacher.schedule("Monday", "10:00-12:00")
magic_teacher.schedule("Monday", "14:00-16:00")
magic_teacher.schedule("Friday", "10:00-12:00")

magic_teacher.check_schedule()
magic_teacher.check_day("Monday")
magic_teacher.check_salary()

Student_Frodo = Student("Frodo", "Baggins", 20)
Student_Frodo.introduce()
Student_Frodo.add_subject("Middle-Earth Geography")

# Task 2


class Mathematician:

    def square_nums(self, my_lis: list) -> list:
        square_nums = map(lambda x: x**2, my_lis)
        return list(square_nums)

    def remove_positives(self, my_lis: list) -> list:
        remove_positives = filter(lambda x: x < 0, my_lis)
        return list(remove_positives)

    def filter_leaps(self, my_lis: list) -> list:

        def leap_years(num: int) -> bool:
            return (num % 4 == 0 and num % 100 != 0) or num % 400 == 0

        filter_leaps = filter(leap_years, my_lis)
        return list(filter_leaps)


m = Mathematician()

print(m.square_nums([7, 11, 5, 4]))
print(m.remove_positives([26, -11, -8, 13, -90]))
print(m.filter_leaps([2001, 1884, 1995, 2003, 2020]))


# Task 3


class Product:

    def __init__(self, product_type: str, name: str, price: float):
        self.product_type = product_type
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.product_type}: {self.name} - {round(self.price * 1.3)} $"


class ProductStore:

    def __init__(self):
        self.products = {}
        self.fee = 1.3
        self.income = 0

    def add(self, product, amount):
        if not isinstance(product, Product):
            raise CustomException("Invalid product type")
        if not isinstance(amount, int) or amount <= 0:
            raise CustomException("Invalid amount value")
        self.products[product] = self.products.get(product, 0) + amount

    def set_discount(self, identifier, percent, identifier_type=None):
        if not isinstance(percent, int) or percent <= 0 or percent > 100:
            raise CustomException("The discount percent must be a positive integer between 1 and 100.")
        if identifier_type:
            for pr in self.products.keys():
                if pr.product_type == identifier_type:
                    pr.price *= (100 - percent) / 100
        else:
            for pr in self.products.keys():
                if pr.name == identifier:
                    pr.price *= (100 - percent) / 100

    def sell_product(self, product_name: str, amount: int):
        for pr, v in self.products.items():
            if pr.name == product_name:
                if v >= amount:
                    self.products[pr] = v - amount
                    self.income += (amount * self.fee * pr.price)
                else:
                    raise CustomException("Not enough products in stock")

    def get_income(self):
        print(self.income)

    def get_all_products(self):
        if len(self.products) == 0:
            print("There are no products in the store")
        else:
            for k, v in self.products.items():
                print(f"{k}: {v} thing")

    def get_product_info(self, product_name: str):
        for pr in self.products.keys():
            if pr.name == product_name:
                return pr.name, self.products[pr]


p = Product('Sport', 'Football T-Shirt', 100)

p2 = Product('Food', 'Ramen', 1.5)

s = ProductStore()

s.add(p, 10)

s.add(p2, 300)

s.get_all_products()

s.get_all_products()

s.get_product_info('Ramen')

s.sell_product('Ramen', 10)

s.sell_product('Football T-Shirt', 10)

s.get_income()

print(s.get_product_info('Ramen') == ('Ramen', 290))
