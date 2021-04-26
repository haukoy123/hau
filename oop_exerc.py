class Vehicle:
    def __init__(self, max_speed, mileage ):
        self.max_speed = max_speed
        self.mileage = mileage


def oop_exerc1():
    modelX = Vehicle(240, 18)
    print(modelX.max_speed, modelX.mileage)
# oop_exerc1()

class Vehicle2:
    color = "white"
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"
    def output(self):
        return f"Color: {self.color}, Vehicle name:{self.name}, Speed: {self.max_speed}, Mileage: {self.mileage}"


class Bus(Vehicle2):
    pass

def oop_exerc3():
    School_bus = Bus("School Volvo", 180, 12)
    print("Vehichle name:", School_bus.name, "speed:", School_bus.max_speed, "mileage:", School_bus.mileage)
# oop_exerc3()



class Bus_execr4(Vehicle2):
    def seating_capacity(self):
        capacity = 50
        return super(Bus_execr4, self).seating_capacity(capacity)
    # def tinh(self):
    #     return  self.max_speed*2

def oop_exerc4():
    a = Bus_execr4("School Volvo", 180, 12)
    print(a.seating_capacity())
    # print(a.tinh())
# oop_exerc4()



class Bus_execr5(Vehicle2):
    def output(self):
        return super(Bus_execr5, self).output()

class Car_execr5(Vehicle2):
   pass


def oop_exerc5():
    bus1 = Bus_execr5("School Volvo", 180, 12)
    car1 =Car_execr5("Audi Q5", 240, 18)
    print(bus1.output())
    print(car1.output())
# oop_exerc5()



class Vehicle6:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

class Bus_execr6(Vehicle6):
    def fare(self):
        a = super(Bus_execr6, self).fare()
        a = a + a*10/100
        return a

def oop_exerc6():
    School_bus = Bus_execr6("School Volvo", 12, 50)
    print("Total Bus fare is:", School_bus.fare())
    print(type(School_bus))

oop_exerc6()
