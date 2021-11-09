import uasyncio as asyncio
from primitives.barrier import Barrier
from machine import UART
import ujson

data = None
async def provider(barrier):
    global data
    n = 0
    while True:
        n += 1  # Get data from some source
        data = ujson.dumps([n, 'the quick brown fox jumps over the lazy dog'])
        print('Provider triggers senders')
        await barrier  # Free sender tasks
        print('Provider waits for last sender to complete')
        await barrier

async def sender(barrier, swriter, n):
    while True:
        await barrier  # Provider has got data
        swriter.write(data)
        await swriter.drain()
        print('UART', n, 'sent', data)
        await barrier  # Trigger provider when last sender has completed

async def main():
    sw1 = asyncio.StreamWriter(UART(1, 9600), {})
    sw2 = asyncio.StreamWriter(UART(1, 1200), {})# ESP32S2 UART(0) is disabled (dedicated to REPL)
    barrier = Barrier(3)
    for n, sw in enumerate((sw1, sw2)):
        asyncio.create_task(sender(barrier, sw, n + 1))
    await provider(barrier)

asyncio.run(main())
