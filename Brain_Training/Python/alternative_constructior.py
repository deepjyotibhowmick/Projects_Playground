class Student:
    school_name= "Ramkrishna Ashram"       #class variable defined here
    num_of_students= 0
    state = "WB"
    def __init__(self,name,roll):
        self.name = name
        self.class_name= 8
        self.roll=roll
        Student.num_of_students += 1
        print(f"{self.name} is a Student number {self.num_of_students}")

    # static method can be built without using self keyword but to let it use while import/inheritance using within class
    @staticmethod
    def full_marks():
        f_marks = 100
        return f_marks
    @classmethod
    def change_state(cls,newstate): #to change class variable which is independent from instance
        cls.state= newstate
    @classmethod
    def stringsplit(cls,str):
        return cls(str.split('_')[0],int(str.split('_')[1]))

    def marks(self,math,sci):
        self.math = math
        self.sci = sci
        print(f"!! {self.state} State Result of School: {self.school_name}!!")
        print(f"{self.name} who is in {self.class_name} standard and roll number {self.roll}, "
              f"got {math} out of {Student.full_marks()} in Math and {sci} out of {Student.full_marks()} in Science\n")

a = Student("Deep",30)
# Suppose we are getting marks in a concatenated string instead of usual instance,
# we need to split it into list and then use existing constructor
a.class_name=10
a.marks(93,80)

strng= "Moni_13"
b=Student.stringsplit(strng) # Using constructor after splitting the value using class method stringsplit
# b.
b.marks(90,70)



