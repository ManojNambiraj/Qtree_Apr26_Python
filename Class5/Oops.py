# OOPs --> Object Oriented Programmings

    # class
    # object
    # Inheritance
    # Polymorphism
    # Encapsulation
    # Abstraction

# class --> template or blueprint of an object

class Car:
    
    def __init__(self, wheels, sheets, color, fuel, speed, names):
        self.no_of_wheels = wheels
        self.no_of_sheets = sheets
        self.color = color
        self.fuel_type = fuel
        self.speed = speed
        self.name = names

    def start(self):
        print("Car is starting")

    def __str__(self):
        return self.name

    def __del__(self):
        print(f"{self} is being destroyed") 

bmw = Car(4, 5, "Red", "Petrol", 200, "bmw")
audi = Car(5, 7, "Black", "Diesel", 220, "audi")

print("BMW Car Details:")

print(bmw.no_of_wheels)
print(bmw.no_of_sheets)
print(bmw.color)
print(bmw.fuel_type)
print(bmw.speed)

print("Audi Car Details:")

print(audi.no_of_wheels)
print(audi.no_of_sheets)
print(audi.color)
print(audi.fuel_type)
print(audi.speed)

