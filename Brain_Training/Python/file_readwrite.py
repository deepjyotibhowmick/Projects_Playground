# ######reading from files-------------
# demo_file = open("Data Science learning note.txt" , "r")

# print(demo_file.readline())
# print(demo_file.readlines()[6])
# print(demo_file.readable())

# print(demo_file.readlines()[4])

# for files in demo_file.readlines():
#     print(files)

# append in the file###
# demo_file = open("Data Science learning note.txt" , "a")
#
# demo_file.write("\nAdding new line at the end of the file")
#
# demo_file.close()

## new file

# demo_file = open("E:\python\code 2023\Demo_file.txt", "a")
#
# demo_file.write("\nthis is a new file of php test")

# for files in demo_file.readlines():
#     print(files)

# demo_file.close()

# read entire file content

# demo_file = open("E:\python\code 2023\Demo_file.txt", "r")
#
# print(demo_file.read())
#
# for files in demo_file:
#     print(files)
# demo_file.close()

with open("E:\python\code 2023\poem.txt", "r") as f:
    print(f.read())
