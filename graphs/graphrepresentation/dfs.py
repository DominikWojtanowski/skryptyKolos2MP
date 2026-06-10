from adjacencyList import *


def dfsRecursive(graph, vertex, res, visitedArr):
    visitedArr[vertex] = True
    res.append(vertex)

    for edge in graph[vertex]:
        if not visitedArr[edge[0]]:
            dfsRecursive(graph, edge[0], res, visitedArr)


def dfsConnected(graph):
    visitedArr = [False] * len(graph)
    res = []

    start = next(iter(graph))

    dfsRecursive(graph, start, res, visitedArr)

    return res


def dfsDisConnected(graph):
    visitedArr = [0] * len(graph)
    res = []

    for key in graph.keys():
        if not visitedArr[key]:
            dfsRecursive(graph, key, res, visitedArr)

    return graph


def dfsIterative(graph):
    visitedArr = [0] * len(graph)
    res = []
    stack = []

    starting = next(iter(graph))
    stack.append(starting)

    while len(stack) > 0:
        curr = stack.pop()

        # If node is already visited, continue
        if visitedArr[curr] == True:
            continue

        res.append(curr)
        visitedArr[curr] = True
        for value in graph[curr]:
            if not visitedArr[value[0]]:
                stack.append(value[0])
    return res


def dfsIterativeGFG(adj):
    n = len(adj)

    visited = [False] * n
    res = []

    st = []
    st.append(0)

    while len(st) > 0:
        curr = st.pop()

        if visited[curr]:
            continue

        visited[curr] = True
        res.append(curr)

        size = len(adj[curr])
        for i in range(size - 1, -1, -1):
            v = adj[curr][i]
            if not visited[v]:
                st.append(v)
    return res
