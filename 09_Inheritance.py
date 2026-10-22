class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age

class Dog(Animal):
    def __init__(self, name, age,breed):
        super().__init__(name, age)
        self.breed = breed

    def display(self):
        print(f"Name of Dog is {self.name} Age is {self.age} and Breed is {self.breed}")

obj = Dog("Butter",20,"Husky")
obj.display()

