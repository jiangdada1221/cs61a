def product(n,term):
    k = 1
    i = 1
    while(i <= n):
        k = term(i)*k
        i = i + 1
    return k
