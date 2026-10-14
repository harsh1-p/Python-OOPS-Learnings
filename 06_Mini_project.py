#Student Managment System 

class Student:

    def __init__(self,name,age,course):
        self.name = name
        self.age = age
        self.course = course

    def display(self):
        print("STUDENT DETAILS\n")
        print("Name : ",self.name)
        print("Age : ", self.age)
        print("Course : ",self.course)

n = int(input("How many Students data you want to enter : "))

student = []

for i in range(n):
    print("Enter details for student",i+1)

    name = input("Enter Name : ")
    age = int(input("Enter age : "))
    course = input("Enter course : ")

    s = Student(name,age,course)

    student.append(s)

for s in student:
    s.display()