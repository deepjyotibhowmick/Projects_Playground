
def without_swap(arry):

    n=len(arry)
    for i in range(1,n):
        insert_index = i
        current_value = arry.pop(i)
        for j in range(i-1,-1,-1):
            if arry[j] > current_value:
                insert_index = j
        arry.insert(insert_index,current_value)
        print(f"Array in step {i}:{arry}")
    print(f"Sorted Array (Insertion sort):{arry}")

def with_swap(arry):

    n=len(arry)
    for i in range(1,n):
        insert_index = i
        current_value = arry[i]
        for j in range(i-1,-1,-1):
            if arry[j] > current_value:
                arry[j+1] = arry[j]
                insert_index = j
            else:  # as left side of the code already sorted, so we don't need to check all the left side elements.
                break
        arry[insert_index] = current_value
        print(f"Array in step {i}:{arry}")
    print(f"Sorted Array (Insertion sort):{arry}")


arry = [15, 12, 3, 45, 87, 2, 75, 95, 13]
# print(f"Unsorted Array:{arry}")
without_swap(arry)
# with_swap(arry)
# Time complexity would be O(n^2) as after one loop, the array is looped through again and again n times.
# This means there are n⋅n comparisons done in total, so the time complexity for Bubble Sort is: n^2

# 12,15,3-2
