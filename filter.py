def filter(func, iterable):
    if func is None:
        for iter in iterable:
            if iter:
                yield iter
    else:
        for iter in iterable:
            if func(iter):
                yield iter


x = lambda y: y % 2 == 0
ls = [1, 6, 8, 9, 10, 0]
print(list(filter(x, ls)))
print(list(filter(None, ls)))
