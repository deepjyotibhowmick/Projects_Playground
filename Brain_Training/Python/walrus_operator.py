name= ["Deep","Moni","Nannu","Rajib","Vundu"]

while (n:= len(name)) >0 :  #here n:= is walrus operator to assign value
    print(name)
    name.pop()

car=[]
# while True:
#     cars=input("Please insert cars name. If you want to stop enter quit: ")
#     if cars=='quit':
#         break
#     car.append(cars)
# print(car)

# replacing with walrus operators
while (cars:=input("Please insert cars name. If you want to stop enter quit: ")) != 'quit':
    car.append(cars)
print(car)

