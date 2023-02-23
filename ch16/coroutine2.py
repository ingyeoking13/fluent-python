# http://www.dabeaz.com/coroutines/cobroadcast.py

def func():
    yield 3
    yield 2
    yield 1

co = func()
for i in co:
    print(i)


def func2():
    x = yield
    print(x)

co2 = func2()
next(co2)
co2.send(13)