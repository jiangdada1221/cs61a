
def two_of_three(a,b,c):
    f = min(a,b,c)
    if a == f :
        return b * b + c * c
    elif b == f :
        return a * a + c * c
    else :
        return a * a + b * b
