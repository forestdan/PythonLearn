a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# length of the list
print("the length of this list is " + str(len(a)))
# access the list
print(a[0])
print(a[1])
print(a[2])
# access all elements of the list
print(a)
# add elements to the list
a.append(11)
print(a)
# add elements to the position
a.insert(1, 13)
print(a)
# delete the end of the list
a.pop()
print(a)
# delete the position of the list
a.pop(1)
print(a)