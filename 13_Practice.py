'''Create an abstract class called Vehicle.

Requirements:
- Create an abstract method called start().
- Create two child classes: Car and Bike.
- Car should print "Car is starting!".
- Bike should print "Bike is starting!".
- Create an object of each class and call start().'''

from abc import ABC,abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car is starting")

class Bike(Vehicle):
    def start(self):
        print("Bike is starting")

obj1 = Car()
obj1.start()


obj2 = Bike()
obj2.start()