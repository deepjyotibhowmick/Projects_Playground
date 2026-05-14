import logging
import time
import math

def greet(fx):
    def mfx():
        print("Hello! Good morning")
        fx()
        print("Thanks for using. Good night")
    return mfx
def greet_param(fx):
    def mfx(x,y):
        print("Hello! Good morning")
        fx(x,y)
        print("Thanks for using Decorator. Good night")
    return mfx
def get_time_diff(fn):
    def mfn():
        start=time.time()
        fn()
        end =time.time()
        diff=end-start
        print(f"Total time taken by this task: {diff}")
    return mfn

def get_time_diff_parm(fn):
    def mfn(*args):
        start=time.time()
        fn(*args)
        end =time.time()
        diff=end-start
        print(f"Total time taken by this task: {diff}")
    return mfn

@greet
@get_time_diff
def essay():
    print("This essay is about the great writer Rabindranath Tagore")
def fact():
    n = 12
    factors = set()
    print(f"sqrt of {n}: {int(math.sqrt(n))} ")
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            factors.add(i)
            factors.add(n // i)
    print(f"Factors are: {factors}")
@greet_param
@get_time_diff_parm
def add(a,b):
    print(f"addition of {a} and {b} = {a+b}")


# essay()
# add(2,3)

fact()

#  Positional arguments. take tuple as an argument
print(".........Positional arguments............")
def arg(*args):
    for i in args:
        print(i)

arg("rajib","deep","Moni","Baby")

# keyword arguments, take dictionary as argument
print("Keyword arguments")
def kwarg(**kwargs):
    for key,value in kwargs.items():
        print(f"key:{key} | value: {value}")

kwarg(name="rajib", salary=2500, location="Kolkata")

