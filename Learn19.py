class student(object):
    
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def printInfo(self):
        print("Student's name is %s, score is %s" % (self.__name, self.__score))
    
    def get_grade(self):
        score = self.__score
        if score >= 90:
            return "A"
        elif score >= 60:
            return "B"
        else:
            return "C"

    
s1 = student("John", 55)
s1.printInfo()
print(s1.get_grade())
# print(s1.__name)
