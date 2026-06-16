def medianOfMedians(A, i):
    sublists = [A[j : j + 5] for j in range(0,len(A),5)]
    medians = [sorted(sublist)[len(sublist)/2] for sublist in sublists]

    if len(medians) <= 5:
        pivot = medians[len(medians)/2]
    else:
        pivot = medianOfMedians(medians, len(medians)/2)
    
    low = [j for j in A if j < pivot]
    high = [j for j in A if j > pivot]

    k = len(low)

    if i < k:
        return medianOfMedians(low, i)
    elif i > k:
        return medianOfMedians(high, i - k - 1)
    else:
        return pivot