# -*- coding: utf-8 -*-

class Student(object):
    
    __score = 0
    
    @property
    def score(self):
        print("Student.scoreGetter is be called")
        return self.__score
    
    @score.setter
    def score(self, value):
        print("Student.scoreSetter is be called")
        if not isinstance(value, int):
            raise ValueError("Score must be an integer!")
        if value < 0 or value > 100:
            raise ValueError("Score must between 0 ~ 100")
        self.__score = value

s = Student()
s.score = 60
print(s.score)