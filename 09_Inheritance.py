class Vehicle():
    def drive(self):
        print("Vehicle is driving")

class Car(Vehicle):
    def start(self):
        print("Car is starting")


obj = Car()
obj.drive()
obj.start()