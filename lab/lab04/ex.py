def count_stairs(n,k):
    if n== 0:
        return 0
    if n < 1:
        return 0
    if n == 1:
        return 1

    return count_stairs(n-1,k) + count_stairs(n-1,k-1)
