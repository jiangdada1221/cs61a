def g(n):
    if n <= 3:
        return n
    else:
        return g(n-1) + 2 * g(n - 2) + 3 * g(n - 3)

def g_iter(n):
    if n <= 3:
        return n
    else:
        i = 4
        a,b,c = 1,2,3
        while i <= n:
            a,b,c = b,c,(c + 2 * b + 3 * a)
            i += 1
        return c
         
