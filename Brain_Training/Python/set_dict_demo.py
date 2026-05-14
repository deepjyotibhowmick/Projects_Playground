list1 =[2,4,5,6,7,3,4,2,5]
set1= {2,4,5,6,7,3,4,2,5}
set2= {2,4,5,14,25,2,5}
set3=  {14,25}
# set4={} # if blank it would be considered as  dictionary
# print(type(set4))
print("This is list:",end="")
print(list1)
list1.sort()
print("This is sorted list:",end="")
print(list1)
print("This is set1:",end="")
print(set1)
print("This is set2:",end="")
print(set2)
print(f"union of set 1&2: {set1.union(set2)}")
print(f"Intersection of set 1&2: {set1.intersection(set2)}")
print(f"check superset:{set2.issuperset(set3)}")
set2.remove(4)
print(f"updated set2:{set2}")
# set2.remove(4) # will raise error as value not present
set2.discard(4) # This will not give us error. to skip error use this
print("Checking if errors..")

dict1= {101: 56, 113:54, 106:85,109:750}
dict2 = {202:456, 205:365}
dict1.update(dict2)
print(dict1)
dict1.pop(101)
print(dict1)
print(dict1[113])