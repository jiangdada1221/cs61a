
def hailstones(n):
    length = 1
    while n != 1:
        print(n)
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
        length = length + 1
    print(1)
    return length
