class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def move(self):
        print("I am moving in Animal Class")

class Dog(Animal):
    def __init__(self, name, age,breed):
        super().__init__(name, age)
        self.breed = breed

    def move(self):
        print("I am moving in Dog class")


obj = Animal("Butter",20)
obj.move()

obj1 = Dog("Butter",30,"Husky")
obj1.move()

print(obj1.name)