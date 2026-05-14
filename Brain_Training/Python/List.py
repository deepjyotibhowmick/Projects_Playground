# from VARIABLE import salary
from enum import Enum


friends = ['kp', 'kali', 'rana', 'bacho']
mixlist = ['test', 2, True]

print(friends)
print(type(friends))
print(mixlist)
print(mixlist[1])
print(friends[3])
print(friends[-2])

print(friends[1:3])

friends[2] = 'Maam'
friends.append('new')
print(friends)
friends.reverse()
print(friends)


class Color(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'

color = Color(input("Enter your choice of 'red', 'blue' or 'green': "))

match color:
    case Color.RED:
        print("I see red!")
    case Color.GREEN:
        print("Grass is green")
    case Color.BLUE:
        print("I'm feeling the blues :(")
