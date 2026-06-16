def bruteForce(capacity,n):
    if n == 0 or capacity == 0:
        return 0
    
    if weights[n - 1] > capacity:
        return bruteForce(capacity,n-1)
    else:
        includingItem = values[n-1] + bruteForce(capacity-weights[n-1], n-1)
        excludingItem = bruteForce(capacity,n-1)
        return max(includingItem, excludingItem)


def memoization(capacity, n):
    if memo[n][capacity] is not None:
        return memo[n][capacity]

    if n == 0 or capacity == 0:
        result = 0
    else:
        if weights[n-1] > capacity:
            result = memoization(capacity, n-1)
        else:
            includingItem = values[n-1] + memoization(capacity - weights[n-1], n-1)
            exlcudingItem = memoization(capacity, n-1)
            result = max(includingItem, exlcudingItem)
    memo[n][capacity] = result
    return result

def tabulation(capacity, n):
    n = len(values)
    tab = [[0 for i in range(capacity + 1)] for j in range(n + 1)]

    # ide od najmniejszego numeru przedmiotu do najwiekszego
    # numeru przedmiotu
    for i in range(1, n+1):
        # ide od najmiejszej nie zerowej dostepnej przestrzeni
        # do domyslnej dostepnej przestrzeni
        for c in range(1, capacity + 1):
            if weights[i-1] <= c:
                including_item = values[i-1] + tab[i-1][c - weights[i-1]]
                excluding_item = tab[i-1][c]
                tab[i][c] = max(including_item, excluding_item)
            else:
                tab[i][c] = tab[i-1][c]
    
    items_included = []
    w = capacity
    for i in range(n, 0, -1):
        if tab[i][w] != tab[i-1][w]:
            items_included.append(i-1)
            w -= weights[i-1]

    return tab[n][capacity]



values = [300, 200, 400, 500]
weights = [2, 1, 5, 3]
capacity = 10
n = len(values)

memo = [[None]*(capacity + 1) for _ in range(n + 1)]

print("\nMaximum value in Knapsack =", knapsack_memoization(capacity, n))