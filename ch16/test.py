a = 1
def d():
    global a
    b = a
    print(b)
    b+=1
    print(b)

def c():
    d()

def my_test():
    a = 3
    c()
    print(a)

my_test()