import uasyncio as asyncio
from uasyncio import Lock

async def task(i, lock):
    while 1:
        async with lock:
            print("Acquired lock in task", i)
            await asyncio.sleep(0.5)
 
async def main():
    lock = asyncio.Lock()  # The Lock instance
    for n in range(1, 4):
        asyncio.create_task(task(n, lock))
    await asyncio.sleep(10)

asyncio.run(main())  # Run for 10s