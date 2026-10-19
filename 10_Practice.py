class Employee():
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def info(self):
        print("Name : ",self.name)
        print("Salary : ",self.salary)


class Manager(Employee):
    def __init__(self,name,salary,department):
        super().__init__(name,salary)
        self.department = department

    def details(self):
        self.info()
        print("Department : ",self.department)


obj = Manager("Harsh",100000,"IT")
obj.details()
