import math

# Task 1

class Animals:

    def __init__(self, name):
        self.name = name

    def talk(self):
        raise NotImplementedError("Must be implemented by sub class")


class Dog(Animals):

    def talk(self):
        print("woof woof")


class Cat(Animals):

    def talk(self):
        print("meow meow")


def animal_talks(animal):
    animal.talk()


dog = Dog("Max")
cat = Cat("Helikopter")
animal_talks(dog)
animal_talks(cat)


# Task 2

class Library:
    def __init__(self, name: str, books: list = None, authors: list = None):
        self.name = name
        self.books = books
        self.authors = authors
        self.dict_books = {}
        for a, b in zip(self.authors, self.books):
            name_book, year_book = repr(b).split(": ")
            self.dict_books.setdefault((a, int(year_book)), []).append(name_book)

    def new_book(self, name_new_book: str, year_new_book: int, author_new_book):
        self.dict_books.setdefault((author_new_book, int(year_new_book)), []).append(name_new_book)
        self.books.append(name_new_book)
        print("New book was added")

    def group_by_author(self, author) -> list:
        lis_by_author = []
        for k, v in self.dict_books:
            if k[0] == repr(author):
                lis_by_author.append(v)
        return lis_by_author

    def group_by_year(self, year: int) -> list:
        lis_by_author = []
        for k, v in self.dict_books:
            if k[1] == year:
                lis_by_author.append(v)
        return lis_by_author

    def __repr__(self):
        return f"{self.name}"

    def __str__(self):
        return f"{self.name}, have {len(self.books)} books"


class Book:

    def __init__(self, name: str, year: str, autor):
        self.name = name
        self.year = year
        self.autor = autor

    def __repr__(self):
        return f"{self.name}: {self.year}"

    def __str__(self):
        return f"{self.name}, autor {self.autor.name}: {self.year}"


class Author:

    def __init__(self, name: str, country: str, books: list = None):
        self.books = books
        self.name = name
        self.country = country

    def __repr__(self):
        return f"{self.name}"

    def __str__(self):
        return f"{self.name},  country: {self.country}, books : {', '.join(self.books)}"


Rowling = Author("Joanne", "UK", ["Harry potter and the philosopher's stone", "The Ickabog"])
Tolkien = Author("Jon", "UK", ["Hobbit", "Lord of the Rong", "Silmarillion"])

Harry_Potter = Book("Harry potter and the philosopher's stone", "1997", Rowling)
Ickabog = Book("The Ickabog", "2020", Rowling)
Hobbit = Book("Hobbit", "1937", Tolkien)

My_library = Library("Bohdan library",
                     [Harry_Potter, Ickabog],
                     [Rowling, Rowling])

My_library.new_book("Dune", 1980, Tolkien)
My_library.new_book("The Ickabog", 2020, Rowling)


# Task 3

class Fraction:

    def __init__(self, numerator: int, denominator: int):
        if type(numerator) != int and type(denominator) != int:
            raise TypeError
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError
        na, da = self.numerator, self.denominator
        nb, db = other.numerator, other.denominator
        gcd = math.gcd(da, db)
        if gcd == 1:
            return Fraction(na * db + nb * da, da * db)
        new_n = na * (db // gcd) + nb * (da // gcd)
        gcd2 = math.gcd(new_n, (da // gcd))
        if gcd2 == 1:
            return Fraction(new_n, (da // gcd) * db)
        return Fraction(new_n // gcd2, ((da // gcd) * db) // gcd2)

    def __sub__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError
        na, da = self.numerator, self.denominator
        nb, db = other.numerator, other.denominator
        gcd = math.gcd(da, db)
        if gcd == 1:
            return Fraction(na * db - nb * da, da * db)
        new_n = na * (db // gcd) - nb * (da // gcd)
        gcd2 = math.gcd(new_n, (da // gcd))
        if gcd2 == 1:
            return Fraction(new_n, (da // gcd) * db)
        return Fraction(new_n // gcd2, ((da // gcd) * db) // gcd2)

    def __mul__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError
        na, da = self.numerator, self.denominator
        nb, db = other.numerator, other.denominator
        gcd = math.gcd(na * nb, da * db)
        return Fraction((na * nb) // gcd, (da * db) // gcd)

    def __truediv__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError
        na, da = self.numerator, self.denominator
        nb, db = other.numerator, other.denominator
        gcd = math.gcd((na * db), (da * nb))
        if da * nb < 0:
            return Fraction(-(na * db) // gcd, -(da * nb) // gcd)
        return Fraction((na * db) // gcd, (da * nb) // gcd)

    def __str__(self):
        return f"{self.numerator} / {self.denominator}"


a = Fraction(1, 4)
b = Fraction(2, 7)
print(Fraction(1, 4) + Fraction(2, 7))
print(Fraction(1, 4) - Fraction(2, 7))
print(Fraction(1, 4) * Fraction(2, 7))
print(Fraction(1, 4) / Fraction(2, 7))
