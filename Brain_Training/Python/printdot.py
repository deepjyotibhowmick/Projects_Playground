import time

def printsdot(no):
    for i in range(no):
        print(".", end="", flush=True)
        time.sleep(1)

if __name__=="__main__":
    printsdot(5)
    # pass

# for i in printsdot(5):
#     print(f"testing dots {i}")
