"""Python comprehensions provide a concise, readable way to create
new collections (lists, dictionaries, sets, or generators) from existing iterables.
They replace longer, multi-line for loops with a single line of optimized code."""
import sys

square=[]
def comprehension_less():

    for i in range(11):
        square.append(i**2)
    print(square)

def list_comp_example() -> list[int]:
    square = [n**2 for n in range(10)]
    return square
def list_comp_example2() -> list[int]:
    square = [n**2 for n in range(10) if n%2==0]
    return square

comprehension_less()
print(f"With comprehension: {list_comp_example()}")
print(f"With comprehension using filter example: {list_comp_example2()}")

def dict_comp_example() -> dict:
    cube = {f"cube of {n}":n**3 for n in range(10) if n%2==1}
    return cube

print(f"With dictionary comprehension: {dict_comp_example()}")

def generator_example():
    serial = (i for i in range (1000000))
    print(next(serial))
    print(next(serial))

generator_example()

def mem_size():
    # A list comprehension materializes 1,000,000 floats immediately in RAM
    large_list = [float(i) for i in range(1000000)]
    print(f"List size in RAM : {sys.getsizeof(large_list) / (1024 * 1024):.2f} MB")  # ~8 MB

    # A generator expression creates a recipe to stream 1,000,000 floats
    large_generator = (float(i) for i in range(1000000))
    print(f"Generator size in RAM: {sys.getsizeof(large_generator)} bytes")         # ~216 bytes!

    # A dictionary expression creates a recipe to stream 1,000,000 floats
    large_dict = {i: float(i) for i in range(1000000)}
    print(f"Dictionary size in RAM: {sys.getsizeof(large_dict)/(1024 * 1024):.2f} MB")             # ~40.00 MB!

mem_size()