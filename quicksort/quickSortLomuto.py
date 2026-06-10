import random


def partitionLomutoStart(arr, l, r):
    pivot = arr[r]
    i = l
    for j in range(l, r):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[r] = arr[r], arr[i]
    return i


def partitionLomutoBeforeStart(arr, l, r):
    pivot = arr[r]
    i = l - 1
    for j in range(l, r):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return i + 1


def quickSort(arr, l, r):
    if l >= r:
        return

    pi = partitionLomutoBeforeStart(arr, l, r)
    # lub partitionLomutoStart

    quickSort(arr, l, pi - 1)
    quickSort(arr, pi + 1, r)
