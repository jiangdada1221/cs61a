#recursion
def make_repeater(f,n):

    def a(x):
    #     i = n     这是错的 只能调用复函数的值，不能当变量更改
    #     if i == 0:
    #         return x
    #     else:
    #         i = i - 1
    #         x = f(x)
    #         return a(x)
    # return a
        i = n
        g = f
        return b(g,x,i)
    return a
def b(f,x,i):
    if i == 0:
        return x
    else:
        x = f(x)
        return b(f,x,i - 1)
triple = lambda x: 3 * x
