from math import sqrt
def squares(s):
    return [round(sqrt(x)) for x in s if round(sqrt(x)) == sqrt(x)]
