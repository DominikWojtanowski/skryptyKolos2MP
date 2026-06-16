import math
def floydmarshall(dist):
    for k in range(len(dict)):
        for i in range(len(dict)):
            for j in range(len(dict)):
                if dist[i][k] != math.inf and dist[k][j] != math.inf:
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
