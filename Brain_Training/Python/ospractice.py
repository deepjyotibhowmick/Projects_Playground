import os as o

path = "E:/Projects_Playground/Projects/Python"
file_name = "Newtest"
# def check_global():
#     global file_name
#     file_name = "testingYaar" # this will change global variable
#     print(file_name)

def filecreationexample():
    for i in range(1,11):
        if (not o.path.exists((f"{path}/{file_name}{i}"))):
            o.mkdir(f"{path}/{file_name}{i}")
def listfolders():

    cwd=o.getcwd()
    # print(cwd)
    # print(path)
    # print(o.listdir(path))
    return (o.listdir(path))
    # print(type(o.listdir(path)))
def removedir():

    for i in range(1,5):
        folder = f"{file_name}{i}"
        fullpath= o.path.join(path,folder)
        o.removedirs(fullpath)
        print(f"deleting dir: {folder=}")

def list_of_elements(fol):
    folders = fol()
    for folder in folders:
        print(f"Inside of {folder} is: ",end="")
        print(o.listdir(f"{path}/{folder}")) # to print the elements of the folder
# calling functions
# filecreationexample()
# print("after creation of folders:",end='')
# print(listfolders())
# removedir()
# print("after deletion of folders:",end='')
# print(listfolders())
list_of_elements(listfolders)

