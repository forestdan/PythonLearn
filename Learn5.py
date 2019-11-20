namelist = ["Tommy", "John", "Amy"]
for item in namelist:
    print(item)
# test range()
"""
numList = list(range(100))
for item in numList:
    print(item)
"""
# test range in loop
sum = 0
for x in range(101):
    sum = sum + x
print(sum)

## test while
sum = 0
n = 100
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

## test break
n = 100
while n > 0:
    if n < 10:
        break
    n = n - 2
    print(n)