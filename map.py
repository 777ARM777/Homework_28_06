def map(func, iterable):
    for iter in iterable:
        yield func(iter)


x = lambda y: y ** 2
ls = [1, 3, 5, 8, 9]
print(list(map(x, ls)))