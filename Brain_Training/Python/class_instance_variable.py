# this is regarding class and instance variable and their precedence of usage
class Student:
    school_name= "Ramkrishna Ashram"       #class variable defined here
    num_of_students= 0
    state = "WB"
    def __init__(self,name):
        self.name = name
        self.class_name= 8
        Student.num_of_students += 1
        print(f"{self.name} is a Student number {self.num_of_students}")

    # static method can be built without using self keyword but to let it use while import/inheritance using within class
    @staticmethod
    def full_marks():
        f_marks = 100
        return f_marks

    @classmethod
    def change_state(cl,newstate): #to change class variable which is independent from instance
        cl.state= newstate

    def marks(self,math,sci):
        self.math = math
        self.sci = sci
        print(f"!! {self.state} State Result of School: {self.school_name}!!")
        print(f"{self.name} who is in {self.class_name} standard, "
              f"got {math} out of {Student.full_marks()} in Math and {sci} out of {Student.full_marks()} in Science\n")


a = Student("Deep")
a.class_name=10 # whatever assigning through object/instance is called instance variable and it has high precedence
Student.marks(a,sci=90,math=93) #everytime object call a method of class, it's execute like this, first send its object name

b = Student("Moni")
b.school_name ="Rohini High"
b.change_state("West Bengal") # this is just replacing while on the go but to change the state value permanently use classmethod decorator
b.marks(80,85)

