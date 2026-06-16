def lomuto(arr, low, high):
    x = arr[high]

    i = low
    for j in range(low, high):
        if arr[j] >= x:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i

def kthSmallest(arr, l, r, k):
    if (k > 0 and k <= r - l + 1):

        index = lomuto(arr,l,r)

        if (index - l == k - 1):
            return arr[index]
        
        if (index - l > k - 1):
            return kthSmallest(arr, l, index - 1, k)
        
        return kthSmallest(arr, index + 1, r, k - index + l - 1)

        