def accumulate(combiner,base, n, term):
    i = 1
    while i <= n:
        base = combiner(base,term(i))
        i += 1
    return base
