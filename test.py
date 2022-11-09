from timeit import timeit


def test_lookups(iterable):
    for i in range(1000):
        if i in iterable:
            pass


setup = "from __main__ import test_lookups; iterable = set(range(10000))"
print(timeit("test_lookups(iterable)", setup=setup, number=100))
setup = "from __main__ import test_lookups; iterable = list(range(10000))"
print(timeit("test_lookups(iterable)", setup=setup, number=100))
