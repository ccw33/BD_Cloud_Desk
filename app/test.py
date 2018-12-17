# encoding:utf-8
import random
from random import randint
from random import choice
import bisect
import timeit

random.seed(5)
lst = [randint(1, 100) for _ in range(500000)]
lst.sort()
val = choice(lst)
val


def binary_search_recursion(lst, val, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if lst[mid] < val:
        return binary_search_recursion(lst, val, mid + 1, end)
    if lst[mid] > val:
        return binary_search_recursion(lst, val, start, mid - 1)
    return mid


def binary_search_loop(lst, val):
    start, end = 0, len(lst) - 1
    while start <= end:
        mid = (start + end) // 2
        if lst[mid] < val:
            start = mid + 1
        elif lst[mid] > val:
            end = mid - 1
        else:
            return mid
    return None

def test_recursion():
     return binary_search_recursion(lst, val, 0, len(lst) - 1)

def test_loop():
     return binary_search_loop(lst, val)

import timeit
t1 = timeit.timeit("test_recursion()", setup="from __main__ import test_recursion")
print(t1)
t2 = timeit.timeit("test_loop()", setup="from __main__ import test_loop")
print(t2)

def binary_search_bisect(lst, val):
    i = bisect.bisect(lst, val)
    if i != len(lst) and lst[i] == val:
        return i
    return None


def test_bisect():
    return binary_search_bisect(lst, val)


t3 = timeit.timeit("test_bisect()", setup="from __main__ import test_bisect")
print(t3)
