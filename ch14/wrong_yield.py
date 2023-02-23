def yield_value(i):
    yield i

def hi(): 
    i = 0
    while True:
        i+=1
        yield from yield_value(i)

print(hi())