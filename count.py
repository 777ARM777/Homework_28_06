calls = 0
def count():
    """Returns the number of times the function has been called"""
    def func():
        global calls
        calls += 1
        print(calls)

    return func


x = count()
x()
y = count()
y()
z = count()
z()



