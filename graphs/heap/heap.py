def heapyfi(arr, index, end):
    assert index >= 0 and index < end

    if (index + 1) * 2 - 1 >= end:
        return

    left = (index + 1) * 2 - 1
    right = (index + 1) * 2
    maxIdx = 0

    if right < end:
        if arr[right] > arr[left]:
            maxIdx = right
        else:
            maxIdx = left
    else:
        maxIdx = left

    if arr[index] < arr[maxIdx]:
        arr[index], arr[maxIdx] = arr[maxIdx], arr[index]
    else:
        return

    heapyfi(arr, maxIdx, end)


def createHeap(arr):
    assert len(arr) > 0

    starting_point = len(arr) // 2 - 1

    for index in range(starting_point, -1, -1):
        heapyfi(arr, index, len(arr))


def peek(arr):
    return arr[0]


def extract_extreme(arr):
    assert len(arr) > 0
    extreme = arr[0]
    arr[0], arr[-1] = arr[-1], arr[0]

    arr.pop()

    heapyfi(arr, 0, len(arr))
    return extreme


def heapsort(arr, ascending=True):
    if not ascending:
        for i in range(len(arr)):
            arr[i] = -arr[i]
    createHeap(arr)
    for i in range(len(arr)-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapyfi(arr, 0, i)

    if not ascending:
        for i in range(len(arr)):
            arr[i] = -arr[i]
