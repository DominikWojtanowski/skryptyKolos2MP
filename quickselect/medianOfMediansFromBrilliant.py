def medianOfMedians(arr, i):
    sublists = [arr[j:j+5] for j in range(0, len(arr), 5)]
    medians = [sorted(oneList)[len(oneList)//2] for oneList in sublists]
    pivot = 0
    if len(medians) > 5:
        pivot = medianOfMedians(medians, len(medians)//2)
    else:
        pivot = sorted(medians)[len(medians)//2]

    low = [j for j in arr if j < pivot]
    high = [j for j in arr if j > pivot]
    pivots = [j for j in arr if j == pivot]

    k = len(low)

    if i < k:
        return medianOfMedians(low, i)
    elif i < k + len(pivots):
        return pivot
    else:
        return medianOfMedians(high, i - k - len(pivots))
