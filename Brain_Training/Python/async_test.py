import asyncio

async def fetch_data(id, delay):
    print(f"Task {id}: Starting...")
    await asyncio.sleep(delay) # Simulates a slow I/O operation
    print(f"Task {id}: Done!")
    return f"Data from {id}"

async def main():
    # Run multiple tasks concurrently
    results = await asyncio.gather(
        fetch_data(1, 2),
        fetch_data(2, 3)
    )
    print(results)

asyncio.run(main())
