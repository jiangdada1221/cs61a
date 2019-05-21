from q1 import has_seven

def pingpong(n):
    if n <= 6:
        return n
    return direction(n) + pingpong(n-1)

def direction(n):
    if n <= 6:
        return 1
    if (n-1) % 7 == 0 or has_seven(n-1):
        return -1 * direction(n-1)
    return direction(n-1)
