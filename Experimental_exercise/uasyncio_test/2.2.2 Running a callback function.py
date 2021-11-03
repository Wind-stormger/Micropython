import uasyncio as asyncio

async def schedule(cbk, t, *args, **kwargs):
    await asyncio.sleep(t)
    cbk(*args, **kwargs)

def callback(x, y):
    print('x={} y={}'.format(x, y))

async def bar():
    asyncio.create_task(schedule(callback, 3, 42, 100))
    for count in range(6):
        print(count)
        await asyncio.sleep(1)  # Pause 1s

asyncio.run(bar())