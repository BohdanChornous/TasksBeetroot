import calendar

# Task 1

string = input("Enter some string")

my_dict = {}
for i in string.split():
    my_dict[i] = my_dict.get(i, 0) + 1

print(my_dict)

# Task 2

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

print(sum([s*p for s, p in zip(stock.values(), prices.values())]))

# Task 3

print(*[(i, i**2) for i in range(1, 11)])

# Task 4

lis_week_day = list(calendar.day_name)

dict_week_day = {k: v for k, v in enumerate(lis_week_day, 1)}

dict_week_day_reversed = {v: k for k, v in dict_week_day.items()}

print(lis_week_day)
print(dict_week_day)
print(dict_week_day_reversed)
