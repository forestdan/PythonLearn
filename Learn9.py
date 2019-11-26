# from collections.abc import Iterable

# str = "ABC"
# print(isinstance(str, Iterable))
# for s in str:
#     print(s)

testList = [1, 5, 3, 2, 4, 7]
def findTheMax(testList):
    max = -1
    min = 65535
    for num in testList:
        if num > max:
            max = num
        if num < min:
            min = num
    result = (min, max)
    return result

print(findTheMax(testList))