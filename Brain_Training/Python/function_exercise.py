"""
1>> Write a function called calculate_area that takes base and height as an input and returns and area of a triangle.
Equation of an area of a triangle is: area = (1/2)*base*height
"""
"""
2>> Modify above function to take third parameter shape type. 
It can be either "triangle" or "rectangle". Based on shape type it will calculate area.
"""
def area_triangle(base,height):
    area = (1 / 2) * base * height
    return area
def area_square(w,l):
    area = w * l
    return area

# print("Please insert the base(feet) and height(feet) of the Triangle/Square you want to create")
#
# selection: str
# base = float(input("Insert Base: "))
# height = float(input("Insert Height: "))
#
# selection = str.lower(input("Please select the shape: \n (a) Triangle \n (b) Square\n Choice:"))
#
#
# if selection != 'a' and selection != 'b':
#     print("You have entered wrong value. Hence selecting Triangle by default.")
#     selection = 'a'
#
#
# if selection == 'a':
#     Total_area = round(area_triangle(base,height),2)
#     print("The Area of the Triange is", Total_area, "feet")
# else:
#     Total_area = round(area_square(base,height),2)
#     print("The Area of the Square is", Total_area, "feet")


def print_pattern(row:int):

    for i in range(1 , row+1):
        for j in range(i,row):
            print(i)



# no_row = int(input("please enter the number of rows: "))

# print_pattern(no_row)
for i in range(1,5):
    s = ""
    for j in range(i):
        s += "*"
        print(s)



# print("*")
# print("**")
# print("***")
# print("****")





