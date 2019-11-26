from functools import reduce

# def f(x):
#     return x * x

# l = [1, 2, 3, 4, 5]
# l = map(f, iter(l))

# p = list(l)
# print(p)

# print(list(map(str, p)))

# def add(x, y):
#     return x + y

# l = list(range(0, 101))
# print(reduce(add, l))

# def transToLower(x):
#     y = ""
#     if isinstance(x, str):
#         y = x.capitalize()
#     return y

# l = ['adam', 'LISA', 'barT']
# print(list(map(transToLower, l)))

# def chen(x, y):
#     return x * y

# l = [3, 5, 7, 9]
# print(reduce(chen, l))


d = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, ".": 0}

def str2float(s):
    i = s.index(".")
    biggerResult = reduce(biggerThanOne, list(map(findInDict, s[0:i])))
    lowerResult = reduce(lowerThanOne, list(map(findInDict, s[-1:i - 1:-1])))
    return biggerResult + lowerResult
    
def findInDict(s):
    return d[s]

def biggerThanOne(x, y):
    return x * 10 + y

def lowerThanOne(x, y):
    return x * 0.1 + y

print(str2float("123.456"))