from typing import List, Tuple


# We assume that all lists passed to functions are the same length N


# answers
# 1 - n question4 1 loop
# 2 - 1 question2 no loop
# 3 - n^2 question5 2 loop
# 4 - n question1 1 loop
# 5 - n^2 question3 2 loop
# 6 - log n question6 The value of i is cut in half each time through the loop
# so it will only take log n iterations.

def question1(first_list: List[int], second_list: List[int]) -> List[int]:
    res: List[int] = []
    for el_first_list in first_list:
        if el_first_list in second_list:
            res.append(el_first_list)
    return res


def question2(n: int) -> int:
    for _ in range(10):
        n **= 3
    return n


def question3(first_list: List[int], second_list: List[int]) -> List[int]:
    temp: List[int] = first_list[:]
    for el_second_list in second_list:
        flag = False
        for check in temp:
            if el_second_list == check:
                flag = True
                break
        if not flag:
            temp.append(second_list)
    return temp


def question4(input_list: List[int]) -> int:
    res: int = 0
    for el in input_list:
        if el > res:
            res = el
    return res


def question5(n: int) -> List[Tuple[int, int]]:
    res: List[Tuple[int, int]] = []
    for i in range(n):
        for j in range(n):
            res.append((i, j))
    return res


def question6(n: int) -> int:
    while n > 1:
        n /= 2
    return n
