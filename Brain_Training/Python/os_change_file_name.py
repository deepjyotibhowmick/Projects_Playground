import os
print(os.getcwd())
fpath="E:\python\code_2023\pic"
os.chdir(fpath)
print(os.getcwd())

def listoffile():
    for file in os.listdir(os.getcwd()):
        print(file)

def change_filename(startname,filepath):
    os.chdir(filepath)
    print(f"We are under file location: {os.getcwd()}")
    i=1
    for file in os.listdir(os.getcwd()):
       fileformat = os.path.splitext(file)[1]
       vstartname=startname+str(i)+fileformat
       print(f"File name has been changed from {file} to {vstartname}")
       os.rename(file,vstartname)
       i +=1

# listoffile()
change_filename("File",fpath)