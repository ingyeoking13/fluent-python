import asyncio

async def coroutine():
    i =0 
    while True:
        i+=1
        yield i

async def main():
    print('hi')
    # yield from coroutine()
    async for i in coroutine():
        yield i
    # yield from coroutine()
    # yield from coroutine()
    # yield from coroutine()


