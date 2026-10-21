# Create a class named Student (blueprint)
class Student:

    # Define a method to display student details
    def display(self, name, age): 
        print("Name:", name)
        print("Age:", age)

# Create the first object of Student class
s1 = Student()

# Call the method for the first student
s1.display("Rahul", 20)

# Create the second object of Student class
s2 = Student()

# Call the method for the second student
s2.display("Priya", 19)