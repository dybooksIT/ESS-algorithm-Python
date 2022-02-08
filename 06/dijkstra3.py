import heapq

def dijkstra(edges, num_v):
    dist = [float('inf')] * num_v
    dist[0] = 0
    q = []
    heapq.heappush(q, [0, 0])

    while len(q) > 0:
        # ヒープから取り出し
        _, u = heapq.heappop(q)
        for i in edges[u]:
            if dist[i[0]] > dist[u] + i[1]:
                # 頂点までのコストが更新できれば更新してヒープに登録
                dist[i[0]] = dist[u] + i[1]
                heapq.heappush(q, [dist[u] + i[1], i[0]])

    return dist

# 辺のリスト（終点とコストのリスト）
edges = [
    [[1, 4], [2, 3]],
    [[2, 1], [3, 1], [4, 5]],
    [[5, 2]],
    [[4, 3]],
    [[6, 2]],
    [[4, 1], [6, 4]],
    []
]
print(dijkstra(edges, 7))
