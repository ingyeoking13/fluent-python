def simple_coroutine():
    print('-> coroutine started')
    x = yield 13
    print('-> coroutine received: ', x)

my_coro = simple_coroutine()
print( my_coro ) 
print(next( my_coro ))
# my_coro.send(42)
my_coro.send(22)


def simple_coroutine2(a):
    print('-> Started: a =', a)
    b = yield a
    print('-> Received: b =', b)
    c = yield a + b
    print('-> Received: c=', c)

my_coro = simple_coroutine2(14)
from inspect import getgeneratorstate
print( getgeneratorstate(my_coro) )
next(my_coro)
print( getgeneratorstate(my_coro) )
my_coro.send(28)
my_coro.send(55)
print( getgeneratorstate(my_coro) )

