def generator_example():
    for i in range(10):
        yield i
gen = generator_example()
for i in gen:
    print(i)

#  we can use as a sequence generator in program design
