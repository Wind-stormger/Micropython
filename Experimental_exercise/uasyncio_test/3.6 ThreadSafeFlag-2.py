from machine import Pin, Timer
import uasyncio as asyncio

class AsyncPin:
    def __init__(self, pin, trigger):
        self.pin = pin
        self.flag = asyncio.ThreadSafeFlag()
        self.pin.irq(lambda pin: self.flag.set(), trigger, hard=True)

    async def wait_edge(self):
        await self.flag.wait()

async def foo():
    pin_in = Pin('X1', Pin.IN)
    async_pin = AsyncPin(pin_in, Pin.IRQ_RISING)
    pin_out = Pin('X2', Pin.OUT)  # Toggle pin to test
    t = Timer(-1, period=500, callback=lambda _: pin_out(not pin_out()))
    await asyncio.sleep(0)
    while True:
        await async_pin.wait_edge()
        print('Got edge.')

asyncio.run(foo())
