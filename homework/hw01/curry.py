def add1(x):
    return x + 1
def times2(x):
    return x * 2
def add3(x):
    return x + 3


def cycle(f1,f2,f3):
    """
    >>> def add1(x):
    ...     return x + 1
    >>> def times2(x):
    ...     return x * 2
    >>> def add3(x):
    ...     return x + 3
    >>> my_cycle = cycle(add1, times2, add3)
    >>> identity = my_cycle(0)
    >>> identity(5)
    5
    >>> add_one_then_double = my_cycle(2)
    >>> add_one_then_double(1)
    4
    """
    def g(n):
        if n == 0:
            return lambda x: x
        if n ==1:
            return lambda x: f1(x)
        if n ==2:
            return lambda x: f2(f1(x))
        if n>= 3:
            f = lambda x: f3(f2(f1(x)))
            n = n - 3
        while n >= 3:
            n = n - 3

            f = lambda x: f3(f2(f1(f(x))))
        if n == 1:
            return lambda x: f1(f(x))
        elif n == 2:
            return lambda x: f2(f1(f(x)))
        else:
            return f
    return g

a = cycle(add1,times2,add3)
