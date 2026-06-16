memo = [None] * 7
def F(n):
    if memo[n] is not None:
        return memo[n]
    else:
        if n <= 1:
            memo[n] = n
        else:
            memo[n] = F(n - 1) + F(n - 2)
    return memo[n]