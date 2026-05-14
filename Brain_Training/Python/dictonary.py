def monthConv():
    monthConversion = {
        "Jan": "January",
        "Feb": "February",
        "Mar": "March",
        "Apr": "April",
        "May": "May",
        "Jun": "June",
        "Jul": "July",
        "Aug": "August",
        "Sep": "September",
        "Oct": "October",
        "Nov": "November",
        "Dec": "December"
    }
    # monthConversion['extra']="This is extra month"
    # monthConversion.pop('extra')
    # monthConversion["Aug"]="AUGUST"
    for ind in monthConversion:
        print(ind,end=': ')
        print(monthConversion[ind])

def dictOps():
    population = {
        "China": 143,
        "India": 137,
        "USA": 32,
        "Pakistan": 21
    }

    userq = input("Please enter your choice from the below: \n(a) Print \n(b) Add\n(c) Remove\n(d)Query\n")
    a: str
    if userq == "a":
        # for ind in population:
        #     print(ind,"==>",population[ind])
        for ind,val in population.items():
            print(ind,"==>",val)
    elif userq == "b":
        new_coun = str(input("Please insert a new country name:"))
        value_found = population.get(new_coun)
        if value_found == None:
            new_pop = int(input("Please enter the population:"))
            population[new_coun] = new_pop
            for ind in population:
                print(ind, "==>", population[ind])
        else:
            print("Country Already Exist")
    elif userq == "c":
        for ind in population:
            print(ind, "==>", population[ind])
        rmov = str(input("Please enter the country name to delete from Dict: "))
        del population[rmov]
        print("Updated Dictionary: ")
        for ind in population:
            print(ind, "==>", population[ind])

    elif userq == "d":
        print(f"Country List: ")
        for index in population:
            print(index)
        slctd_cntry = str(input("Please enter the Country name to check population:"))
        print("Population of the Country ",slctd_cntry,"is :",population[slctd_cntry])
    else:
        print("Wrong choice, Try again....")
def dict2d():
    statesIn=["WB","TN","MP","MH"]
    statesUS=["California","Texas","Floria"]
    nation= {"India":statesIn,
             "USA": statesUS}
    for ind in nation:
        print(ind,end=':')
        print(nation[ind])
# dictOps()
# # monthConv()
# dict2d()

dict1={'a':1,
       'b':2}
dict2={'b':2,
       'a':1}
if dict1==dict2:
    print("Dictionary is same")
else:
    print("Dictionary is not same")