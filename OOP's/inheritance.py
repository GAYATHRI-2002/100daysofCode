class Animal:
    def __init__(self,name):
        self.name = name
        self.is_sleep = True

    def is_speek(self):
        print(f"{self.name} will speek")
    def is_eating(self):
        print(f"{self.name} is eating")

class Dog(Animal):
    pass

class Cat(Animal):
    pass

obj1 = Dog("scooby")
obj2 = Cat("Millo")
print(obj1.name)
print(obj1.is_sleep)
obj1.is_eating()
obj1.is_speek()



