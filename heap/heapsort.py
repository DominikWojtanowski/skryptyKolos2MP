def heapyfi(arr, n, i):
    l = (i + 1) * 2 - 1
    r = (i + 1) * 2 

    largest = i

    if l < n and arr[l] > arr[largest]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r
    
    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]
        heapyfi(arr,n,largest)

def heapsort(arr,n):

    # najpierw tworzymy heap
    # zaczynamy od n // 2 - 1
    # bo to pierwszy nie lisc
    # wiec to pierwszy element
    # ktory moze nie spelniac wymagan
    # kopca, idziemy do 0
    for i in range(n // 2 - 1, -1, -1):
        heapyfi(arr,n,i)

    # najwiekszy element idzie na koniec
    # i heapyfiujemy ten element ktory
    # zaswapowalismy za niego
    for i in range(n - 1, -1, 0):
        arr[i], arr[0] = arr[0], arr[i]
        heapyfi(arr, i, 0)