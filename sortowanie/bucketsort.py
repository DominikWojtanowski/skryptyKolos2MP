def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -=1
        arr[j + 1] = key
        
def bucketSort(arr):
    # tutaj bedziemy uzywac bucket sorta
    # dla ulamkow
    # normalnie to uzywamy jakiegos innego przedzialu
    # np k = sqrt(len(arr))
    buckets = [[] for i in range(len(arr))]
    for value in arr:
        # normalnie to jest jak do interpolacji
        # tylko bez low bo low jest stale
        # i wynosi 0
        # dajemy dla k - 1 poniewaz dla x = max(arr) z k
        # wyjdzie pos = k czyli bedzie index error
        # wiec dajemy k - 1
        # czyli pos = ((x - min(arr)) * (k - 1)) // (max(arr) - min(arr))
        bi = int(value * len(arr))
        buckets[bi].append(value)

    for bucket in buckets:
        insertionSort(bucket)

    index = 0
    for bucket in buckets:
        for value in bucket:
            arr[index] = value
            index += 1

        

