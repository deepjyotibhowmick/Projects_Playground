flag='No issue'
try:
    number = int(input("Enter a number: "))
    print(f"You entered: {number} and result of 100/{number} is :{round(100/number)}")

except ZeroDivisionError as err:
    # print("Division can't be by 0.")
    print("The error is: ",err)
    flag='Exception occurred'
except ValueError as err:
    # print(" You entered invalid number: ")
    print("The error is: ", err)
    flag='Exception occurred'
finally:

    print(f"{flag}, Just testing Finally!!")