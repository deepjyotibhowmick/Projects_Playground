
def forPrac():
    num= (1,2,3,4,5,6)
    for numc in num:
        print(numc)

    my_str = ["Raj", "Deep", "Sam", "Ranp", "Moni"]

    for numc in range(2,10):
        print(numc)

    for index in range(len(my_str)):
        print(my_str[index])

    for ind in my_str:
        print(ind)
    for i in range(0, 100, 5):
        print(i)
# forPrac()

def expo():
    res = 1
    getNum = int(input("Enter a number: "))
    getPow = int(input("Enter power: "))
    for index in range(getPow):
        res = res * getNum
    return res

# print("exponential result of: ", expo())

def binarySearch(lis, num):
    left= 0
    right= len(lis)
    mid = int(round((left + right) / 2))
    print(f"mid is: {mid}")
    while (mid>=left or mid<=right):
        mid = int(round((left + right) / 2))
        if (lis[mid]==num):
            print(f"Item found at index: {mid}")
            break
        elif (lis[mid]>num):
            right = mid - 1
        elif (lis[mid]<num):
            left = mid + 1
        else:
            print("Item not found in the list.")


numlist = [2, 5, 6, 8, 3, 4, 18, 9, 54, 78]
print(numlist)
numlist.sort()
print("sorted list: ",end='')
print(numlist)
# binarySearch(numlist,8)
for index,va in enumerate(numlist): # to get the index and value together during loop
    print(f"numlist[{index}] = {va}")

