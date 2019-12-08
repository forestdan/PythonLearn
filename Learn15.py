# def lazy_sum(*args):
#     def sum():
#         ax = 0
#         for n in args:
#             ax = ax + n
#         return ax
#     return sum

# # print(lazy_sum)
# # print(lazy_sum([n for n in range(0, 101)]))

# print(lazy_sum(1, 2, 3, 4, 5, 6, 7)())

def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        fs.append(f)
    return fs

f1, f2, f3 = count()

print(f1())
print(f2())
print(f3())