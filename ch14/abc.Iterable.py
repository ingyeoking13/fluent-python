class Foo:
    def __iter__(self):
        pass

from collections import abc
print( issubclass(Foo, abc.Iterable) )
f = Foo()
print( isinstance(f, abc.Iterable) ) 
