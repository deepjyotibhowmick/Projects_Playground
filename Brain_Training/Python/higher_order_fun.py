import math


def sum(n1,n2):
    return n1+n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2
def min(n1,n2):
    return (n1-n2)
# print (div(5,2)) : normal method to call a function

def calculation(n1,n2,operation):
    return operation(n1,n2)
#  Higher order function to call another function using a func as a parameter
print(f"Using higher order function: {calculation(10,5,mul)}")

sqr = lambda x: x*x
sqrt = lambda  x: math.sqrt(x)

print(f"using lambda function: {sqr(2)}")
print(f"using lambda function: {sqrt(36)}") 
# write formula of (a+b)^2 = a^2 +2ab+ b^2
a_plus_b_sqr= lambda x,y: sqr(x)+2*x*y+sqr(y)
print(f"using lambda function (a+b)^2 [a=2,b=3] : {a_plus_b_sqr(2,3)}")
