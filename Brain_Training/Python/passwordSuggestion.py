import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def passSugg1():
    password = []
    for i in range(2,20):
        if i%3==0 or i%5==0:
            random_n = random.choice(numbers)
            password.append(random_n)
        if i%2==0 or i%7==0:
            random_l = random.choice(letters)
            password.append(random_l)
        if i%9==0 or i%10==0:
            random_s = random.choice(symbols)
            password.append(random_s)
    random.shuffle(password)
    print("".join(password))
    del password
print("We have a password suggestion for you: ",end='')
passSugg1() #easy one
