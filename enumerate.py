def enumerate(iterable, start=0):
    for iter in iterable:
        yield start, iter
        start += 1


ls = [1, 5, 6, 8, 9]
print(list(enumerate(ls, 11)))
print(list(enumerate(ls)))
