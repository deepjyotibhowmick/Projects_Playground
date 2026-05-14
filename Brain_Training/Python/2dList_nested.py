# 2d array
number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]

test_grid = [
    ["*"],
    ["*","*"]
]
print(test_grid)
number_grid[3][0] = 3
# number_grid.append(new_no)

print("number grid 2d: ")
print(number_grid[0][0])
print(number_grid[2][1])
print(number_grid[3][0])
# print(number_grid[3][1])
# nested for loop
print("Print Grid : \n")
for row in number_grid:
    print(row)

for row in test_grid:
    print(row)

print("Print in a series : \n")
for row in number_grid:
    for col in row:
        print(col)
