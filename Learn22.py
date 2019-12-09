# -*- coding: utf-8 -*-

class Student(object):
    
    name = ""
    
    score = 0

    def get_name(self):
        return self.name
    
    def get_score(self):
        return self.score

s = Student()
print(s.get_name())
print(s.get_score())