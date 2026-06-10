def partitionLomuto(arr, l, r):
    i = l - 1
    pivot = arr[r]
    for j in range(l, r):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[r] = arr[r], arr[i+1]
    return i + 1


def selectionSort(arr):
    for i in range(0, len(arr)):
        maxIdx = 0
        for j in range(0, len(arr) - i):
            if arr[j] > arr[maxIdx]:
                maxIdx = j
        arr[maxIdx], arr[len(arr) - i - 1] = arr[len(arr) - i - 1], arr[maxIdx]


def findMedian(arr):
    chunkOfFives = [arr[j:j + 5] for j in range(0, len(arr), 5)]
    medians = [sorted(oneChunk)[len(oneChunk)//2] for oneChunk in chunkOfFives]

    if len(medians) <= 5:
        return sorted(medians)[len(medians)//2]

    return findMedian(medians)


def medianOfMediansOSpaceComplexity(arr, l, r, k):
    if k < l or k > r:
        return -1

    if l == r:
        return arr[l]
    pivot = findMedian(arr[l:r+1])

    pivotPos = arr.index(pivot, l, r + 1)

    arr[r], arr[pivotPos] = arr[pivotPos], arr[r]

    partitionedPivotPos = partitionLomuto(arr, l, r)

    if partitionedPivotPos == k:
        return arr[partitionedPivotPos]
    elif partitionedPivotPos > k:
        return medianOfMediansOSpaceComplexity(arr, l, partitionedPivotPos - 1, k)
    else:
        return medianOfMediansOSpaceComplexity(arr, partitionedPivotPos + 1, r, k)
