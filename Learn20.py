class Animal(object):
    
    def run(self):
        print("Animal is running.....")
    
class Dog(Animal):
    
    def run(self):
        print("Dog is running.....")

class Cat(Animal):
    
    def run(self):
        print("Cat is running.....")

a = Animal()
# a.run()
# d = Dog()
# d.run()
# c = Cat()
# c.run()
# print(isinstance(c, Animal))
# print(isinstance(a, Dog))

# def run_twice(animal):
#     animal.run()
#     animal.run()

# run_twice(a)
# run_twice(d)

print(type(a))