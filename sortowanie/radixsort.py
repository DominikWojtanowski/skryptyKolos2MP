def countingsort(arr, exp):
    n = len(arr)

    carr = [0] * 10
    rarr = [0] * n

    for i in range(0,n):
        v = arr[i] // exp
        carr[v % 10] += 1
    
    for i in range(1,10):
        carr[i] += carr[i - 1]

    i = n - 1
    while i >= 0:
        v = arr[i] // exp
        rarr[carr[v % 10] - 1] = arr[i]
        carr[v % 10] -= 1
        i -= 1
    
    i = 0
    for i in range(0, n):
        arr[i] = rarr[i]

def radixSort(arr):
    mv = max(arr)
    exp = 1

    while mv / exp >= 1:
        countingsort(arr,exp)
        exp *= 10