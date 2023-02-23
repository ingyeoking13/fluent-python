from typing import Coroutine, List

coroutines : List[Coroutine] = []

def add(name: str):
    co = listener(name)
    next(co)
    coroutines.append(co)

def eventaggreagtor():
    while True:
        data = yield
        print(f'message queue listened. {data}')
        for co in coroutines:
            d = yield from co
            print(f'{d[0]} listend {d[1]} times')

def listener(name):
    count = 0
    while True:
        da = yield (name, count)
        print(f'I\'m {name}. listened {da}')
        count += 1

def main():
    ea = eventaggreagtor()
    add('flower')
    add('james')
    add('yohan')
    next(ea)
    ea.send("hi!")
    ea.send("bloom")

main()

