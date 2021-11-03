import uasyncio as asyncio

async def bar(x):
    count = 0
    while True:
        count += 1
        print('Instance: {} count: {}'.format(x, count))
        await asyncio.sleep(1)  # Pause 1s

async def main():
    for x in range(3):
        asyncio.create_task(bar(x)) # just create_task,not run
    print('Tasks are running') # run
    await asyncio.sleep(10)# Perform each task in sequence

asyncio.run(main())
