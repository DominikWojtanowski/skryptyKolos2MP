def lomutoPartition(arr, low, high):
    n = high
    pivot = arr[n - 1]

    i = -1
    for j in range(low, n):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[n-1] = arr[n - 1], arr[i + 1]
    return i + 1

def hoarePartition(arr, low, high):
    n = high
    pivot = arr[low]

    i = low - 1
    j = n

    while True:
        while True:
            i += 1
            if arr[i] >= pivot:
                break
        while True:
            j -= 1
            if arr[j] < pivot:
                break
    
        if i < j:
            break

        arr[i], arr[j] = arr[j], arr[i]

    


def quicksort(arr, low, high):
    if low < high:
        pi = lomutoPartition(arr,low,high)

        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)
