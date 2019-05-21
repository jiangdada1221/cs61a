"""this is a python"""
from operator import add,sub


def absab(a, b):
    if b<0:
        f=sub
    else:
        f=add
    return f(a,b)
