class Student:
    def __init__(self,name):
        self.__name = name
        print(f"{self.__name} is a Student")

    # static method can be built without using self keyword but to let it use while import/inheritance using within class
    @staticmethod
    def full_marks():
        f_marks = 100
        return f_marks

    def marks(self,math,sci):
        self.math = math
        self.sci = sci
        print(f"{self.__name} got {math} out of {Student.full_marks()} in Math and {sci} out of {Student.full_marks()} in Science")



a = Student("Deep")
b = Student("Moni")
# print(a.__name) # we can't access some attribute mentioned with "__" in the beginning
# print(a._Student__name) # we can access private variable by using name of class along with single underscore (_)
# print(a.full_marks())
# a.marks(93,90)
Student.marks(a,93,90) #everytime object call a method of class, it's execute like this, first send its object name
print(a.__dir__())
b.marks(80,85)

