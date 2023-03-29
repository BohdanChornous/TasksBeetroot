# Task 1

def bubble_sort_2(lis: list) -> None:
    n = len(lis)
    left = 0
    right = n - 1
    direction = True

    while direction:
        direction = False

        for i in range(left, right):
            if lis[i] > lis[i + 1]:
                lis[i], lis[i + 1] = lis[i + 1], lis[i]
                direction = True
        right -= 1

        for i in range(right, left, -1):
            if lis[i] < lis[i - 1]:
                lis[i], lis[i - 1] = lis[i - 1], lis[i]
                direction = True
        left += 1


my_list = [5, 2, 8, 3, 1, 6]
bubble_sort_2(my_list)
print(my_list)

# Task 2


def merge_sort(lis: list) -> None:
    if len(lis) > 1:
        left_lis = lis[:len(lis)//2]
        right_lis = lis[len(lis)//2:]
        merge_sort(left_lis)
        merge_sort(right_lis)
        i = 0
        j = 0
        k = 0
        while i < len(left_lis) and j < len(right_lis):
            if left_lis[i] < right_lis[j]:
                lis[k] = left_lis[i]
                i += 1
            else:
                lis[k] = right_lis[j]
                j += 1
            k += 1
        while i < len(left_lis):
            lis[k] = left_lis[i]
            i += 1
            k += 1
        while j < len(right_lis):
            lis[k] = right_lis[j]
            j += 1
            k += 1


my_list2 = [5, 2, 8, 3, 1, 6]
merge_sort(my_list2)
print(my_list2)

# Task 3


def quicksort(lis: list, left: int, right: int):
    if left < right:
        partition_pos = partition(lis, left, right)
        quicksort(lis, left, partition_pos - 1)
        quicksort(lis, partition_pos + 1, right)


def partition(lis: list, left: int, right: int) -> int:
    i = left
    j = right - 1
    pivot = lis[right]

    while i < j:
        while i < right and lis[i] < pivot:
            i += 1
        while j > left and lis[j] > pivot:
            j -= 1
        if i < j:
            lis[i], lis[j] = lis[j], lis[i]

    if lis[i] > pivot:
        lis[i], lis[right] = lis[right], lis[i]

    return i


my_list3 = [22, 11, 88, 66, 55, 77, 33, 44]
quicksort(my_list3, 0, len(my_list3) - 1)
print(my_list3)
