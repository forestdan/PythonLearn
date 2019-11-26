# ge = (x * x for x in range(0, 101))
# for a in ge:
#     print(a)

# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield b
#         a, b = b, a + b
#         n = n + 1
#     return "done"

# f = fib(6)
# while(True):
#     try:
#         g = next(f)
#         print("g=", g)
#     except StopIteration as e:
#         print("function return value=", e)
#         break

# a = [1, 2, 3, 4, 5]
# result = []
# result.append(a[0])
# for index, value in enumerate(a):
#     if index == len(a) - 1:
#         result.append(a[index])
#         continue
#     result.append(a[index] + a[index + 1])

# print(result)
def test(max):
    n = 1
    oldResult = [1]
    while(n <= max):
        yield oldResult
        newResult = [oldResult[0]]
        for index, value in enumerate(oldResult):
            if index == len(oldResult) - 1:
                newResult.append(oldResult[index])
                oldResult = newResult
                continue
            newResult.append(oldResult[index] + oldResult[index + 1])
        n = n + 1
    return "done"

f = test(6)
while(True):
    try:
        g = next(f)
        print("g=", g)
    except StopIteration as e:
        print("function return value=", e)
        break