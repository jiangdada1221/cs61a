def has_seven(k):
    if k == 0:
        return False
    last_digit = k % 10
    if last_digit == 7:
        return True
    else:
        return has_seven(k // 10)
