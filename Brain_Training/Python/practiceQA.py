# get the sum of given input from the numbers available in the list in how many way possible.
def get_unique_list(args):
    # l1 = [1, 2, 3, 4, 5, 6, 1, 3, 5]
    l1 = args
    unique_list = []
    for i in range (0,len(l1)):
        if l1[i] in unique_list:
            continue
        else :
            unique_list.append(l1[i])
    # print(f"Given list: {l1}")
    # print(f"Unique list: {unique_list}")
    return unique_list

def get_numbers_sum(sum):
    l1 = [1, 2, 3, 4, 5, 6, 1, 3, 5]
    # uni = list(set(l1)) #this is system method using set
    uni = get_unique_list(l1) # this is my method to get unique list
    print(f"Given list: {l1}")
    print(f"Unique list: {uni}")

    newl1=[]
    for i in range(0,len(uni)):
        for j in range(1+i,len(uni)) :
            # print(f"{i} + {j}= {uni[i]} + {uni[j]}")
            if uni[i]+uni[j] == sum:
                 if newl1.count(uni[i]) == 0:
                    newl1.append(uni[i])
                 if newl1.count(uni[j]) == 0:
                    newl1.append(uni[j])
    print(f"Numbers which will be sum equal to {sum}:{newl1}")

def getReverseString():
    s1 = "Hello World"
    print(f"Given string: {s1}")
    print(f"Reverse string: {s1[::-1]}")



if __name__ == "__main__":
    print("I am within main function.. Follow me...")
    get_numbers_sum(8)
    # get_unique_list([1, 2, 3, 4, 5, 6, 1, 3, 5])
