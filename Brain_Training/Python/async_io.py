import asyncio
import time

async def func1():
    await asyncio.sleep(1)
    print("fun1")
async def func2():
    await asyncio.sleep(2)
    print("fun2")
async def func3():
    time.sleep(1)
    print("fun3")

async def main():
    task = asyncio.create_task(func1())
    # await func1()
    await func2()
    await func3()

    l = await asyncio.gather(
        func1(),
        func2(),
        func3()
    )
    print(l)
asyncio.run(main())