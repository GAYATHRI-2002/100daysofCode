from abc import ABC, abstractmethod
class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass
    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def go(self):
        print("You can start the car")
    def stop(self):
        print("you can stop the car")

class Boat(Vehicle):
    def go(self):
        print("You can start the boat")
    def stop(self):
        print("you can stop the boat")


car = Car()
car.go()
car.stop()

boat = Boat()
boat.stop()
boat.go()
