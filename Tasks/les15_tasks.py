# Task 1

class Person:
    def __init__(self, name: str, surname: str, age: str):
        self.name = name
        self.surname = surname
        self.age = age

    def talk(self):
        print(f"Hello my name is {self.name} {self.surname}, and I'm {self.age} years old")


my_person = Person('Bohdan', 'BlackMustache', '23')
my_person.talk()


# Task 2

class Dog:
    age_factor = 7

    def __init__(self, age: int):
        self.age = age

    def human_age(self):
        return self.age * self.age_factor


my_dog = Dog(3)
print(my_dog.human_age())


# Task 3

CHANNELS = ["BBC", "Discovery", "TV1000"]


class TVController:

    def __init__(self, channels: list = None):
        if channels is None:
            channels = CHANNELS
        self.channels = channels
        self.current_channel_index = 0
        self.name_channel = ""

    def first_channel(self) -> str:
        return self.channels[0]

    def last_channel(self) -> str:
        return self.channels[-1]

    def turn_channel(self, turn_to: int) -> str:
        self.current_channel_index = turn_to - 1
        return self.channels[self.current_channel_index]

    def next_channel(self) -> str:
        self.current_channel_index += 1
        if self.current_channel_index >= len(self.channels):
            self.current_channel_index = 0
        return self.channels[self.current_channel_index]

    def previous_channel(self) -> str:
        self.current_channel_index -= 1
        if self.current_channel_index < 0:
            self.current_channel_index = len(self.channels) - 1
        return self.channels[self.current_channel_index]

    def current_channel(self) -> str:
        return self.channels[self.current_channel_index]

    def is_exist(self, name_number) -> str:
        if type(name_number) == str:
            name_channel = name_number
            return "YES" if name_channel in self.channels else "NO"
        else:
            current_channel_index = name_number - 1
            return "YES" if len(self.channels) > current_channel_index >= 0 else "NO"

