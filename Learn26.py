# -*- coding: utf-8 -*-

# try:
#     print("Try....")
#     # r = 10 / 0
#     # r = 10 / int('a')
#     r = 10 / 1
#     print("result:%s" % r)
# except ZeroDivisionError as e:
#     print("expect:", e)
# except ValueError as e:
#     print("Value Error:", e)
# else:
#     print("no error")
# finally:
#     print("finally")
    
# print("End")

class MyValueError(ValueError):
    pass

def errorTestInMethod(a):
    if a < 20:
        raise MyValueError

def errorTestOutMethod(a):
    try:
        errorTestInMethod(a)
    except MyValueError as e:
        print("MyValueError is happenning", e)
    finally:
        print("finally")
    
a = 10
errorTestOutMethod(a)