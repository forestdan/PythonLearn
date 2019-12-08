# -*- coding: utf-8 -*-

# f = lambda x: x * x
# print(f(3))
# print(list(map(f, [1, 3, 5, 7, 9])))

# def build(x, y):
#     return lambda : x * x + y * y

# f = build(3, 4)
# print(f())

L = list(filter(lambda x: x % 2 == 1, range(1, 21)))
print(L)