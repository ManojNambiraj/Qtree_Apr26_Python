# OOPs:

# Encapsulation: --> (getters and setters)

    # Access Specifiers: Public, Private

class Car:
    def __init__(self):
        self.__no_of_wheels = 0
        self.__engine = ""

    def setNo_of_wheels(self, wheels):
        self.__no_of_wheels = wheels

    def getNo_of_wheels(self):
        return self.__no_of_wheels
    
    def setEngine(self, engine):
        self.__engine = engine

    def getEngine(self):
        return self.__engine

honda = Car()

honda.setNo_of_wheels(4)
honda.setEngine("V6")

print(honda.getNo_of_wheels())
print(honda.getEngine())