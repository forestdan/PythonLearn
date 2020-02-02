# -*- coding: utf-8 -*-

# from io import StringIO

# f = StringIO()
# f.write("Hello")
# f.write("  ")
# f.write("World")
# print(f.getvalue())

# from io import StringIO

# f = StringIO("Hi!\nThis is John!\nNice to meet you!")
# while(True):
#     s = f.readline()
#     if s == "":
#         break
#     print(s.strip())

from io import BytesIO

f = BytesIO()
f.write("你好世界".encode("utf-8"))
print(f.getvalue())