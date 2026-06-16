def countingsort(arr):
    # zakladamy ze sa tylko liczby >= 0
    maxV = max(arr)

    carr = [0] * (max(arr) + 1)
    
    for v in arr:
        carr[v] += 1
    
    for idx in range(1,len(carr)):
        carr[idx] += carr[idx - 1]

    rarr = [0] * len(arr)

    for i in range(len(arr)-1, -1, -1):
        v = arr[i]
        rarr[carr[v] - 1] = v
        carr[v] -= 1
    return rarr
           






    