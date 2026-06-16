from math import inf
def maksymalnaPodtablica(arr):
    best = arr[0]
    suma = arr[0]
    for i in range(1,len(arr)):
        suma = max(arr[i], suma + arr[i])
        best = max(suma, best)
    return best
