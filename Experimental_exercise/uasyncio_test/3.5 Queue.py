import uasyncio as asyncio
from primitives.queue import Queue

async def slow_process():
    await asyncio.sleep(2)
    return 42

async def produce(queue):
    print('Waiting for slow process.')
    result = await slow_process()
    print('Putting result onto queue')
    await queue.put(result)  # Put result on queue

async def consume(queue):
    print("Running consume()")
    result = await queue.get()  # Blocks until data is ready
    print('Result was {}'.format(result))

async def queue_go(delay):
    queue = Queue()
    asyncio.create_task(consume(queue))
    asyncio.create_task(produce(queue))
    await asyncio.sleep(delay)
    print("Done")

asyncio.run(queue_go(4))
