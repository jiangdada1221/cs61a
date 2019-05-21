def count_change(amount):
    def count_partitions(n,m):
        if n == 0:
            return 1
        elif n < 0:
            return 0
        elif m == 0:
            return 0
        else:
            return count_partitions(n-m,m) + count_partitions(n,m//2)
    def highest_two(i):
        if i >= amount:
            return i // 2
        else:
            return highest_two(i * 2)
    return count_partitions(amount,highest_two(1))
