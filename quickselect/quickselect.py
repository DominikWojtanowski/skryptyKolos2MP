def partition(arr, l, r):
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


def quickselectNormal(arr, l, r, k):
    if k < 0 or k >= len(arr):
        return -1

    if l == r:
        return arr[l]

    pi = partition(arr, l, r)

    if pi >= k:
        return quickselectNormal(arr, l, pi, k)
    else:
        return quickselectNormal(arr, pi + 1, r, k)


def quickselectnotnormal(arr, l, r, k):
    if k > 0 and k <= r - l + 1:
        index = partition(arr, l, r)

        if index - l == k - 1:
            return arr[index]

        if index - l > k - 1:
            return quickselectnotnormal(arr, l, index - 1, k)
        else:
            return quickselectnotnormal(arr, index + 1, r, k - index + l - 1)
