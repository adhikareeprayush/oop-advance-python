# parent class, car and motorcycle both use this
class Vehicle:
    def general_usage(self):
        print("General usage: Transportation")


# car inherits general_usage from Vehicle
class Car(Vehicle):
    def __init__(self):
        print("I am a Car")
        self.wheels = 4
        self.has_roof = True

    # calls the parent method then prints car specific usage
    def specific_usage(self):
        self.general_usage()
        print("Specific usage: Commute to work, family trips")


# same as Car but for motorcycles
class MotorCycle(Vehicle):
    def __init__(self):
        print("I am a MotorCycle")
        self.wheels = 2
        self.has_roof = False

    def specific_usage(self):
        self.general_usage()
        print("Specific usage: Road trips, racing")


c = Car()
c.specific_usage()

m = MotorCycle()
m.specific_usage()
