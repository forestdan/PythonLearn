# -*- coding: utf-8 -*-

# l = [36, -9, 3, 6, 17, -22]
# print(sorted(l))
# print(sorted(l, key = abs))

# print(sorted(["John", "Tom", "Amy", "Cathelin"]))
# print(sorted(["John", "Tom", "Amy", "Cathelin"], key = str.lower, reverse = True))

def by_name(l):
    return l[0]

def by_age(l):
    return l[1]

L = [("Bob", 75), ("Adam", 92), ("Bart", 66), ("Lisa", 88)]
print(sorted(L, key = by_name))
print(sorted(L, key = by_age, reverse = True))
