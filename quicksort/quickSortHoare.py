def partitionHoare(arr, l, r):
    i = l - 1
    j = r + 1
    pivot = arr[l]
    while True:

        while True:
            i += 1
            if arr[i] >= pivot:
                break

        while True:
            j -= 1
            if arr[j] <= pivot:
                break

        if i >= j:
            return j

        arr[i], arr[j] = arr[j], arr[i]


def quickSort(arr, l, r):
    if l >= r:
        return

    pivot = partitionHoare(arr, l, r)

    quickSort(arr, l, pivot)
    quickSort(arr, pivot + 1, r)
