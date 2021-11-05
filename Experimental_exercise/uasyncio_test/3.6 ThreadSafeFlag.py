import uasyncio as asyncio
from machine import Timer

tsf = asyncio.ThreadSafeFlag()

def cb(_):
    tsf.set()

async def foo():
    while True:
        await tsf.wait()
        # Could set an Event here to trigger multiple tasks
        print('Triggered')

tim = Timer(1)
tim.init(period=1000,callback=cb)
asyncio.run(foo())
