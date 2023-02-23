
def item():
    yield 1
    yield 2
    yield 3
    yield 4

def main():
    yield item()
print(list(main()))
# [<generator object item at 0x10276b120>] 

# def main():
#     yield from item()
# print(list(main()))
# print(main())
# [1, 2, 3, 4]
# <generator object item at 0x10276b120>