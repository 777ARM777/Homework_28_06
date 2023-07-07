def zip(*iterable, strict=False):
    if strict:
        for i in iterable:
            if len(iterable[0]) != len(i):
                raise ValueError("The sizes of the iterables must be the same")
        n = len(iterable[0])
    else:
        n = min(len(i) for i in iterable)
    for i in range(n):
        yield tuple([iterable[j][i] for j in range(len(iterable))])


a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica", "Adam")
c = (125, 95, 852, 52)

x = zip(a, b, c)
print(list(x))
y = zip(a, b, c, strict=True)
print(list(y))

