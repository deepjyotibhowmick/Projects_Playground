from math import *

def basicVarPractice():
    age = 35
    name = "Deep"
    salary = 60000.50
    print(name, " is ", age, " years old and his salary is ", salary)
    # we can't use + operator with different data type, in order to do need to typecast into string
    name = "Raj"
    salary = 70000.50
    print(name + " is " + str(age) + " years old and his salary is\"\""" " + str(salary))
    strn = "Python learning hours"
    print(strn.upper())  # converting upper case
    print(strn[2])  # printing spefic position
    print(strn.index('th'))  # to get position number
    print(strn.replace("Python", "Cobra"))
    print("Total count of o: ", strn.count("o"))
    print(strn.lower().islower())  # checking boolean
    into = 5
    print("MOD: ", 10 % 3)
    print("Div: ", round(10 / 3))

    print("power: ",pow(into, 2))
    print("max: ",max(7, 2, 8, 15))
    print ("sqrt of number: ",round(sqrt(144)))

# basicVarPractice()
