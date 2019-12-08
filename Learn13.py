# -*- coding: utf-8 -*-


# def is_odd(x):
#     return x % 2 == 1

# l = [1, 2, 3, 4, 5, 6, 7, 8]
# l = list(filter(is_odd, l))
# print(l)

# def _odd_iter():
#     n = 1
#     while True:
#         n = n + 2
#         yield n

# def _not_divisable(n):
#     return lambda x : x % n > 0

# def primes():
#     yield 2
#     it = _odd_iter()
#     while True:
#         n = next(it)
#         yield n
#         it = filter(_not_divisable(n), it)

# for n in primes():
#     if n < 1000:
#         print(n)
#     else:
#         break

def is_palindrome(n):
    s = str(n)
    return n - int(s[-1::-1]) == 0

print(is_palindrome(999))
