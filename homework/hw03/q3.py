from operator import add, mul, sub
def filtered_accumulate(combiner,base,pred,n,term):
    if n == base:
        return base
    elif pred(term(n)):
        return combiner(term(n),filtered_accumulate(combiner,base,pred,n-1,term))
    else:
        return filtered_accumulate(combiner,base,pred,n-1,term)

def odd(x):
    return x % 2 ==1

def greater_than_5(x):
    return x > 5
