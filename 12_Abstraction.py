'''Abstraction means hiding the internal details and showing only what is necessary. 
In Python OOP,an abstract class can also set rules that child classes must follow.'''

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Woof!")

dog = Dog()
dog.sound()