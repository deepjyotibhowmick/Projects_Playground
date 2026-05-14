def sayhi():
    print("Hi Developer")


def add(a, b):
    sum = a + b
    print(sum)


def mixf(name, age):
    print("You are", name, " and your age is", age)


# with return statement

def sqrts(num):
    # print(num*num)
    return num * num


# if statement
def iftest(num):

    if num == 0:
        print("You have entered 0")
    elif num % 2 == 0:
        print(num, " is even number bro")
    else:
        print(num, " is odd number bro")


print("This is func")
sayhi()
add(5, 11)
mixf("deep", 32)
print(sqrts(5))

# numb = int(input("Please insert a number: "))
# iftest(int(numb))
# iftest(numb)
print("fibonacci series: ")
def fibo(n):
    a=0
    b=1
    sum=a+b
    print(a)
    print(b)
    while sum<n:
        print(sum)
        a = b
        b = sum
        sum = a + b

fibo(225)


