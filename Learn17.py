# # -*- coding: utf-8 -*-

# 装饰器

# def now():
#     print("9999-12-31")

# f = now
# f()

# print(now.__name__)
# print(f.__name__)

################################################################
# def log(func):
#     def wrapper(*args, **kw):
#         print("call %s():" % func.__name__)
#         return func(*args, **kw)
#     return wrapper

# @log
# def newNow():
#     print("newNow is be called")

## @log 相当于执行了 newNow = log(newNow)
# newNow()
################################################################
# def log(text):
#     def decorator(func):
#         def wrapper(*args, **kw):
#             print("%s %s():" % (text, func.__name__))
#             return func(*args, **kw)
#         return wrapper
#     return decorator

# @log("excute")
# def newNow():
#     print("newNow is be called")

# newNow()
################################################################


# def metric(fn):
#     print("%s executed in %s ms" % fn.__name__, 10.24)

import time

def metric(func):
    def wrapper(*args, **kw):
        t1 = time.time()
        func(*args, **kw)
        t2 = time.time()
        print("%s executed in %s ms" % (func.__name__, (t2 - t1) * 1000))
        return
    return wrapper

@metric
def myTestFunction():
    time.sleep(5)
    return

myTestFunction()