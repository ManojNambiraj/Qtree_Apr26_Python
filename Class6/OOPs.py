# OOPs:

    # Class
    # Object
    # Inheritance
    # Polymorphism
    # Encapsulation
    # Abstraction

# Inheritance:

# from SecondClass import Parent

# Top to Bottom Inheritance:

    # class GrantParent:                             
    #     isAssested = True

    #     def GrantEyesColor(self):
    #         print("This is GrantParent eye color: ", "Blue")

    # class Parent(GrantParent):                          
    #     bankBalance = 100000

    #     def Behavior(self):
    #         print("This is Family behavior: ", "Smiley face")

    # class Child(Parent):                          
    #     packetMoney = 500

    #     def childsHabits(self):
    #         print("This is child Habits: ", "Playing games")

    # sam = Child()

    # print(sam.packetMoney)
    # sam.childsHabits()

    # print("-------------------------------")

    # print(sam.bankBalance)
    # sam.Behavior()

    # print("-------------------------------")

    # sam.GrantEyesColor()
    # print(sam.isAssested)

# Bottom to Top Inheritance:


from SecondClass import Parent

class Child(Parent):
    def __init__(self, Money, balance):
        super().__init__(balance)
        self.packetMoney = Money

    def showPacketMoney(self):
        print("This is child packet money: ", self.packetMoney)

sam = Child(500, 100000)

sam.showPacketMoney()
sam.showBalance()