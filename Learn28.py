# -*- coding: utf-8 -*-

# f = open("/Users/ruixuandan/mylog/nohup.out")
# s = f.read()
# f.close()
# print(s)

# try:
#     f = open("/Users/ruixuandan/mylog/nohup.out")
#     print(f.read())
# except:
#     if f:
#         f.close()

# with open("/Users/ruixuandan/mylog/nohup.out") as f:
#     print(f.read())

# with open("/Users/ruixuandan/mylog/nohup.out") as f:
#     i = 0
#     for line in f.readlines():
#         print("%s------->  %s" % (i, line.strip()))
#         i = i + 1

# with open("/Users/ruixuandan/mylog/text", "x") as f:
#     f.write("Hello World")


with open("/Users/ruixuandan/mylog/IMG_0373.JPG", "rb") as f1:
    with open("/Users/ruixuandan/mylog/MyCopyImage.JPG", "wb") as f2:
        f2.write(f1.read())