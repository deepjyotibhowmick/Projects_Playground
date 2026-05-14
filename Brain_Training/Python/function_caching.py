import time
from functools import lru_cache


@lru_cache
def func_cache(n):
    time.sleep(5)
    return n*n

print(func_cache(5))
print(func_cache(2))
print(func_cache(8))

print(func_cache(5))
print(func_cache(3))
print(func_cache(8))