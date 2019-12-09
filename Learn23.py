# -*- coding: utf-8 -*-

class Student(object):
    
    def __init__(self, name):
        self.__name = name
        
    def get_name(self):
        return self.__name
    
def set_name(self, name):
        self.__name = name
   
s = Student("John")
print(s.get_name())

from types import MethodType
s.set_name = MethodType(set_name, s)

# s.set_name("Amy")
# print(s.get_name())
