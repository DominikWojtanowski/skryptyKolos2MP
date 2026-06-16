from math import inf
def maksymalnaPodtablicaBruteForce(arr):
    best = -inf
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            suma = 0
            for k in range(i,j+1):
                suma += arr[k]
            best = max(suma,best)
    return best