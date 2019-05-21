#loop
def make_repeater(f,n):
    def a(x):
        i = n                # 没有这个赋值 系统会报错
        if i == 0:           # if n == 0:
            return x         #    return x
        while i > 0:         # while n > 0..... n = n -1
            x = f(x)
            i = i - 1
        return x
    return a

triple = lambda x: 3 * x

求make_repeater(triple,5)(1)
