import uasyncio as asyncio
from primitives.semaphore import Semaphore

async def foo(n, sema):
    print('foo {} waiting for semaphore'.format(n))
    async with sema:
        print('foo {} got semaphore'.format(n))
        await asyncio.sleep_ms(200)

async def main():
    sema = Semaphore()
    for num in range(3):
        asyncio.create_task(foo(num, sema))
    await asyncio.sleep(2)

asyncio.run(main())