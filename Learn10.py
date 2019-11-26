print([x * x for x in range(0, 10)])

print([x * x for x in range(0, 10) if x % 2 == 0])

d = {"a": "1", "b": "2", "c": "3"}
print([x + "=" + y for x, y in d.items()])