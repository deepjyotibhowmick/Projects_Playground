def get_numbers_sum(sum):
    l1 = (1, 2, 3, 4, 5, 6, 1, 3, 5)
    uni = list(set(l1))
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
    get_numbers_sum(6)