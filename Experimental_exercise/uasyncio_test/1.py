import uasyncio as asyncio

async def bar(x):
    count = 0
    while True:
        gc.collect()
        count += 1
        print('Instance: {} count: {}'.format(x, count))
        print(gc.mem_alloc())# RAM size has been used
        print(gc.mem_free())#free RAM size
        await asyncio.sleep(1)# Pause 1s
        
async def main():
    for x in range(10):
        asyncio.create_task(bar(x))
    await asyncio.sleep(10)
    
gc.enable()#Enable automatic garbage collection
gc.collect()#Run a garbage collection
asyncio.run(main())