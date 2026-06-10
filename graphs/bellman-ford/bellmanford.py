import math


def bellmanFord(V, E, source):
    dist = [math.inf] * V
    dist[source] = 0

    for i in range(V):
        for u, v, w in E:
            if dist[u] != math.inf and dist[v] > dist[u] + w:
                if i == V - 1:
                    return [-1]

                dist[v] = dist[u] + w

    return dist


def bellmanFord2(V, E, source):
    dist = [math.inf] * V
    dist[source] = 0

    for _ in range(V - 1):
        for u, v, w in E:
            if dist[u] != math.inf and dist[v] > dist[u] + w:
                dist[v] = dist[u] + w

    for u, v, w in E:
        if dist[u] != math.inf and dist[v] > dist[u] + w:
            return [-1]

    return dist
