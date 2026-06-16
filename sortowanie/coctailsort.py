def coctailSort(arr):
    start = 0
    end = len(arr) - 1
    swapped = True
    while (swapped == True):
        swapped = False
        for j in range(start,end):
            if arr[j] > arr[j + 1]:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]
                swapped = True
                
        if not swapped:
            break

        swapped = False

        end -= 1

        for j in range(end - 1, start - 1, -1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        start += 1
               