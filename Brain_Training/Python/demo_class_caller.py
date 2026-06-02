from class_demo import Human
try:
    person1 = Human("Tom Cruise", "actor")
    person2 = Human("Sania Mirza", "tennis player")

    person1.do_work()
    person2.do_work()

    person1.how_famous()
    person2.how_famous()
except TypeError as er:
    print("Error is: ", er)


if __name__ == '__main__':
    person1 = Human("Tom Cruise", "actor")