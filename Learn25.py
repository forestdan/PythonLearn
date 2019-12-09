# -*- coding: utf-8 -*-

class Runnable(object):

    def run(self):
        print(str(type(self)) + "Running")

class Flyable(object):
    
    def fly(self):
        print(str(type(self)) + "Flying")

class Animal(object):
    pass

class Mammal(Animal):
    pass

class Bird(Animal, Flyable):
    pass

class Dog(Mammal, Runnable):
    pass

class Bat(Mammal, Flyable):
    pass

class Parrot(Bird, Flyable):
    pass

class Ostrich(Bird, Flyable):
    pass

b = Bird()
b.fly()

d = Dog()
d.run()