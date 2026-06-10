from adjacencyMatrix import *
from collections import deque


def bfs(graph, vertex, queue, visitedArr, res):

    starting = vertex
    visitedArr[starting] = True
    queue.append(starting)

    while len(queue) > 0:
        curr = queue.popleft()
        res.append(curr)

        for idx, value in enumerate(graph[curr]):
            if value == 1 and not visitedArr[idx]:
                visitedArr[idx] = True
                queue.append(idx)


def bfsDisconnected(graph):
    visitedArr = [False] * len(graph)
    queue = deque()
    res = []

    for idx in range(len(graph)):
        if not visitedArr[idx]:
            bfs(graph, idx, queue, visitedArr, res)
