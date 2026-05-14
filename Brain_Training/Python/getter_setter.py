class MyClass:
    def __init__(self,val):
        self.value = val

    def show(self):
        print(f"value is {self.value}")
    #  constructor overloading using default value to arguments
    # def __init__(self,val1=0,val2=0):
    #     self.value1 = val1
    #     self.value2 = val2

    # getter here :
    @property
    def valu(self):
        return self.value

    @valu.setter
    def valu(self, newval):
        self.value = newval * 10


a = MyClass(20)
# print(a.valu)
a.valu = 65
print(a.valu)
a.show()
# b = MyClass (5,10)
# print(b.value1,b.value2)
