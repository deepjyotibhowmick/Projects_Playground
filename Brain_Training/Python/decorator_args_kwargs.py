import logging
import time
import math

from numpy import random
def arg_example():
#  Positional arguments. take tuple as an argument
# print(".........Positional arguments............")
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

# arg_example()

# Simple decorator without param
def greet(fx):
    def mfx():
        print("Hello! Good morning")
        fx()
        print("Thanks for using. Good night")
    return mfx
def get_time_diff(fn):
    def wrapper():
        start=time.time()
        fn()
        end =time.time()
        diff=end-start
        print(f"Total time taken by this task: {diff}")
    return wrapper

#  decorators with param value limited or using args/kwargs
def greet_param(fx):
    def nfx(x,y):
        print("Hello! Good morning")
        print(f"First param: {x} | Second param: {y}")
        fx(x,y)
        print("Thanks for using Decorator. Good night")
    return nfx
def greet_p(fz):
    # parameter number should be equals to the function's param which is calling decorator otherwise will not work
    # using args, kwargs can be used with any parameter or no param .
    def wrapper(*args,**kwargs):
        print(f"Using decorator: {fz.__name__} is going to execute next")
        fz(*args,**kwargs)
        print(f"Thanks for using decorator!! {fz.__name__} is completed")
    return wrapper

def get_time_diff_parm(fn):
    def wrapper(*args,**kwargs):
        start=time.time()
        fn(*args,**kwargs)
        end =time.time()
        diff=end-start
        print(f"Total time taken by this task: {diff}")
    return wrapper

@greet
@get_time_diff
def essay():
    print("This essay is about the great writer Rabindranath Tagore")
@get_time_diff_parm
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

@get_time_diff_parm
@greet_p
def multiply(a,b,c):
    print(f"multiplication of {a}, {b} and {c} = {a*b*c}")

# essay()
# add(2,3)
# multiply(5,7,2)
# fact()

# Passing parameter while calling decorators. This is very useful while retrying any failure

def retry(max_attempts=3, time_delay=2):
    def decor_retry(func):
        def wrapper(*args, **kwargs):
            attempts = 0
            while (attempts < max_attempts):
                try:
                    # running the Data engineering task
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    print(f"Function {func.__name__} failed. Retrying {attempts} out of {max_attempts} times. {e}")
                    if attempts < max_attempts:
                        print(f"Retrying after {time_delay} seconds..")
                        time.sleep(time_delay)
                    else:
                        print(f"Max retries reached. Closing execution..")
        return wrapper
    return decor_retry

import requests
import json
@retry(max_attempts=4, time_delay=1)
def newsupdate():
    # url= "https://www.google.com"
    query= input("What type of news you are interested in: ")
    url = f"https://newsdata.io/api/1/latest?apikey=pub_072640b42b09427f8bf8130b69b1087f&q={query}"
    r = requests.get(url)
    news = json.loads(r.text)
    print(news,type(news))
    for article in news["results"]:
        print("source_name: ",end=": ")
        print(article["source_name"])
        print("Description: ", end=": ")
        print(article["description"])
        print("Link to read details: ", end=": ")
        print(article["link"])
        print("-------------------------------------------")


# Execute the decorated data pipeline function
if __name__ == "__main__":
    newsupdate()



