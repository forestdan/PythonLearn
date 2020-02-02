# -*- coding: utf-8 -*-

import json

class Student(object):
    
    def __init__(self, name, gender, score):
        self.name = name
        self.gender = gender
        self.score = score

def studentToJson(std):
    return {
        "name": std.name,
        "gender": std.gender,
        "score": std.score
    }

s = Student("John", "M", 18)

print(json.dumps(s, default=studentToJson))