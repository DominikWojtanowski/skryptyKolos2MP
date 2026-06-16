def bubbleSort(arr):
    for i in range(len(arr)):
        changed = False
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                changed = True
        if not changed:
            break