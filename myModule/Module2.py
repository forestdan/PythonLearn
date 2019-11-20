# -*- coding: utf-8 -*-

"This is the doc of module2"

__author__ = "ForestDan"

def _private_1():
    print("This is private1")

def _private_2():
    print("This is private2")

def greeting(value):
    if value > 10:
        _private_1()
    else:
        _private_2()
