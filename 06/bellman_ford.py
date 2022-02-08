def bellman_ford(edges, num_v):
    dist = [float('inf') for i in range(num_v)]
    dist[0] = 0

    changed = True
    while changed:
        changed = False
        for edge in edges:
            if dist[edge[1]] > dist[edge[0]] + edge[2]:
                # 頂点までのコストが更新できれば更新
                dist[edge[1]] = dist[edge[0]] + edge[2]
                changed = True

    return dist

# 辺のリスト（起点、終点、コストのリスト）
edges = [
    [0, 1, 4], [0, 2, 3], [1, 2, 1], [1, 3, 1],
    [1, 4, 5], [2, 5, 2], [4, 6, 2], [5, 4, 1],
    [5, 6, 4]
]
print(bellman_ford(edges, 7))
