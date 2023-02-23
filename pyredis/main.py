from redis.asyncio import Redis, ConnectionPool
import asyncio

def singleton(class_):
  instances = {}
  def getinstance(*args, **kwargs):
    if class_ not in instances:
        instances[class_] = class_(*args, **kwargs)
    return instances[class_]
  return getinstance

@singleton
class Pool:
    def __init__(self) -> None:
        self.conn = ConnectionPool(host='localhost')

class TestClass:
    def __init__(self) -> None:
        self.r = Redis(connection_pool=Pool().conn)
        print(self.r)

    async def keys(self, *args):
        result = await self.r.keys()
        return result
    
    async def set(self, *args):
        if len(args) < 3:
            raise RuntimeError()

        await self.r.hset(args[0], args[1], args[2])

    async def get(self, *args):
        if len(args) < 2:
            raise RuntimeError()
        
        result = await self.r.hget(args[0], args[1])
        return result
    


async def func():
    t = TestClass()
    print(await t.set('1','2', 123))
    print(await t.get('1','2'))

asyncio.run(func())