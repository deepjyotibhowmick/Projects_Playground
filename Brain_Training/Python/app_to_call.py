## class_student == file name and Student is the class defined under class_student file
from typing import List

from class_student import Student
from class_mcq import Questions

student1 = Student("Deep", "CSE", 7.69, True)
student2 = Student("Moni", "CSE", 8.69, False)
student3 = Student("Rahul", "ECE", 7.2, True)

print(student1.name, student1.gpa)
print(student2.name, student2.gpa)

print(student2.name,"is",student2.studentclassification())
print(student1.name,"is",student1.studentclassification())

question_prompt: list[str] = [
    "What is the color of Apple: \n(a) Red/Green \n(b) Orange \n(c) Black \n(d) Yellow \nselect from the above: ",
    "What is the color of Pineapple: \n(a) Red/Green \n(b) Orange \n(c) Black \n(d) Yellow \nselect from the above: ",
    "What is the color of Orange: \n(a) Red/Green \n(b) Orange \n(c) Black \n(d) Yellow \nselect from the above: "
]

# print(question_prompt[2])
question = [
    Questions(question_prompt[0], "a"),
    Questions(question_prompt[1], "d"),
    Questions(question_prompt[2], "b")
]


def check_answer(question):
    score = 0
    for index in question:
        print("\n")
        answer = input(index.ques)
        if answer == index.ans:
            score += 1
    print("You got " + str(score) + " Out of " + str(len(question)) + " correct")


check_answer(question)
