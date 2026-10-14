'''A constructor is a special method that runs automatically when an object is created. It is used to initialize the object's data.'''

# Create a class named Student
class Student:

    # Constructor: runs automatically
    def __init__(self, name):
        self.name = name  # Store the student's name

# Create an object and pass a value
s1 = Student("Rahul")

# Print the student's name
print(s1.name)