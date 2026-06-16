from collections import deque
def bfs(adj):
    if adj is None:
        return None
    
    V = len(adj)
    res = []
    visited = [False] * V
    q = deque()

    visited[0] = True
    q.append(0)

    while q:
        curr = q.popleft()
        res.append(curr)

        for idx in adj[curr]:
            if not visited[idx]:
                visited[idx] = True
                q.append(idx)

    return res
