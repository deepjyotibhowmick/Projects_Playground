class Animal:
    def __init__(self,name,legs):
        self.name=name
        self.legs=legs
class Mammal(Animal):
    def __init__(self,name,legs,is_produce_milk):
        super().__init__(name,legs)     # using immediate parent class functions
        self.is_produce_milk=is_produce_milk

a = Animal("Lion",4)
print(f"{a.name} has {a.legs} legs")
b = Mammal ("Tiger",4,True)
print(f"{b.name} has {b.legs} legs and it produce milk is {b.is_produce_milk}")
