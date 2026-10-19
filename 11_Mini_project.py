class Person():
    def __init__(self,name,age):
        self.name =  name
        self.age = age 

    def details(self):
        print("Name : ",self.name)
        print("Age :",self.age)

class Students(Person):
    def __init__(self, name,age,grade):
        super().__init__(name,age)
        self.grade = grade

    def show_grade(self):
        self.details()
        print("Grade :",self.grade)

class Teacher(Person):
    def __init__(self, name,age,subject):
        super().__init__(name,age)
        self.subject = subject

    def show_subject(self):
        self.details()
        print("Subject : ",self.subject)


obj = Students("Harsh",20,10)
obj.show_grade()

obj2 = Teacher("Aryan",42,"Python")
obj2.show_subject()