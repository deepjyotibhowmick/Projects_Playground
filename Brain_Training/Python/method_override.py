class Shape:
    def  __init__(self,wide,length):
        self.wide = wide
        self.length = length

    def area(self):
        return self.wide*self.length

class Circular(Shape):
    def __init__(self,radius):
        self.radius=radius
        super().__init__((self.radius*3.14),self.radius) # we are using Shape's area calculation method by using Super

    # Normal method to write another function for circle calculation
    # def area(self):
    #     return 3.14*self.radius*self.radius


rect = Shape(5,7)
print(f"Area of rectangle is: {rect.area()}")
circle = Circular(2)
print(f"Area of Circle is: {circle.area()}")
