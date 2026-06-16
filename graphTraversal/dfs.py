def dfsRec(adj, visited, s, res):
    if s is None:
        return res
    
    visited[s] = True
    res.append(s)

    for i in adj[s]:
        if not visited[i]:
            dfsRec(adj,visited, i, res)

def dfs(adj):
    visited = [False] * len(adj)
    res = []
    dfsRec(adj,visited,0,res)
    return res   

def dfsIter(adj):
    n = len(adj)

    visited = [False] * n
    res = []

    st = []
    st.append(0)

    while st:
        node = st.pop()

        if visited[node] == True:
            continue

        visited[node] = True
        res.append(node)

        size = len(adj[node])
        for i in range(size - 1, -1, -1):
            v = adj[node][i]
            if not visited[v]:
                st.append(v)

    return res