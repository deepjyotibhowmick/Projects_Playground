from functools import reduce

# from scipy.special import factorial

list1= [3,4,6,7,9,22,13,35,74]
list2= [1,2,4,5,7,8,9,0]
list3 = ["I", "am","a", "data", "engineer"]

print(list1)
print(list2)

# to get the same calculation for all values in the list use map function instead of loop
# ***map function***
sqrlist1 = list(map(lambda x: x*x, list1)) # need to convert the result into list
print(f"Square of all value inside list{list1} : {sqrlist1}")

# ***filter***
fillis1 = list(filter(lambda x: x%2==0, list1))
print(f"Even numbers of all value inside list{list1} : {fillis1}")

# ***reduce function***

redlis2 = reduce(lambda x,y: x*y, list(filter(lambda x: x>0, list2))) # filtering non-zero from list then reduce
print(f"Multiply of all value inside list{list2} : {redlis2}")

concatlis3= reduce(lambda x,y: x +" " +y, list3)
print(f"concatenation of list3: {concatlis3}")

# factorial using reduce
facto = lambda n: reduce(lambda x,y: x*y,range(1,n+1),1)
print(f"Factorial using reduce: {facto(5)}")

