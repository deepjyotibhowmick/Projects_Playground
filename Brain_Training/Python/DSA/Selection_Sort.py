
def without_swap(arry):
    n=len(arry)
    for i in range(n-1):
        min_val_at_index=i
        for j in range(i+1,n):
            if arry[j] < arry[min_val_at_index]: # use > to sort in descending order
                min_val_at_index = j
        # inserting in the beginning and then swapping all elements one by one from insert point
        # which is little slow
        min_value=arry.pop(min_val_at_index)
        arry.insert(i,min_value)
        print(f"Array in step {i}:{arry}")

    print(f"Sorted Array (Selection sort):{arry}")

def with_swap(arry):
    n=len(arry)
    for i in range(n-1):
        min_val_at_index=i
        for j in range(i+1,n):
            if arry[j] < arry[min_val_at_index]: # use > to sort in descending order
                min_val_at_index = j
        # we are reducing extra swapping by 1 index from minimum index by swapping the values directly
        arry[i],arry[min_val_at_index]=arry[min_val_at_index],arry[i]
        print(f"Array in step {i}:{arry}")

    print(f"Sorted Array (Selection sort):{arry}")

arry = [12,15,3,45,87,2,75,95,13]
print(f"Array:{arry}")
# without_swap(arry)
with_swap(arry)

# Time complexity would be O(n^2) as after one loop, the array is looped through again and again n times.
# This means there are n⋅n comparisons done in total, so the time complexity for Bubble Sort is: n^2
