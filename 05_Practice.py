'''Practice Question: Create a Student Class
Your task: Write a Python program using a constructor.
1. Create a class named Student.
2. Create a constructor __init__() that accepts name and age.
3. Store these values using self.
4. Create an object named s1 with the name "Rahul" and age 20.
5. Print the student's name and age.'''


class student:

    def  __init__(self,name,age):
        self.name = name
        self.age = age


s1 = student("Rahul",20)

print(s1.name)
print(s1.age)