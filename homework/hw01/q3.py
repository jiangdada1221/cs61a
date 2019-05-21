from operator import mod


def largest_factor(n):
    i = 2
    if n == 1:
        return n
    while mod(n, i) != 0:
        i = i + 1
    if i == n:
        return i
    n = n / i
    while mod(n, 2) == 0:
        if n == 2:
            return n
        n = n / 2
    return n
