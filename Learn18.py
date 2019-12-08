# -*- coding: utf-8 -*-

# print(int("11", base=2))

import functools

# ini2 = functools.partial(int, base=2)
# print(ini2("1110000"))

def myPartialTest(*args):
    sum = 0
    for n in args:
        sum = sum + n
    return sum

myPartialTestPlus = functools.partial(myPartialTest, 1000)
print(myPartialTestPlus(1, 2, 3))