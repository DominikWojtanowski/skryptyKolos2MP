from math import inf
def maksymalnaPodtablicaNaiwna(arr):
    best = -inf
    for i in range(len(arr)):
        suma = 0
        for j in range(i,len(arr)):
            suma += arr[j]
            best = max(suma,best)
    return best