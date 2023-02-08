# Task 1

def my_func(func) -> int:
    return len(func.__defaults__)

# Task 2


"""
Реализуйте функцию sort_priority(), которая принимает два аргумента в следующем порядке:
values — список чисел
group — список, кортеж или множество чисел
Функция должна сортировать по неубыванию список чисел values, делая при этом приоритетной группу чисел из group, которая 
должна следовать первой.
"""


def sort_priority(values: list, group: list) -> list:
    new_vals = []
    new_group = []
    for i in values:
        if i in group:
            new_group.append(i)
        else:
            new_vals.append(i)
    values[:] = sorted(new_group) + sorted(new_vals)
    return values


numbers = [150, 200, 300, 1000, 50, 20000]
sort_priority(numbers, [300, 100, 200])

print(numbers)

# Task 3


def square_nums(nums):
    return [num ** 2 for num in nums]


def remove_negatives(nums):
    return [num for num in nums if num > 0]


def choose_func(nums: list, func1, func2) -> list:
    return func1(func2(nums)) if nums == func2(nums) else func2(nums)


nums1 = [1, 2, 3, 4, 5]

nums2 = [1, -2, 3, -4, 5]

print(choose_func(nums1, square_nums, remove_negatives))
print(choose_func(nums2, square_nums, remove_negatives))
