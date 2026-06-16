def TowerOfHanoi(n, fromRod, toRod, auxRod):
    if n == 0:
        return
    TowerOfHanoi(n - 1,fromRod, auxRod, toRod)
    print("...")
    TowerOfHanoi(n - 1,auxRod, toRod, fromRod)