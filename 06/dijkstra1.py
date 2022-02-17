def dijkstra(edges, num_v):
    dist = [float('inf')] * num_v
    dist[0] = 0
    q = [i for i in range(num_v)]

    while len(q) > 0:
        # 가장 비용이 적은 정점을 찾기
        r = q[0]
        for i in q:
            if dist[i] < dist[r]:
                r = i

        # 가장 비용이 적은 정점을 꺼내기
        u = q.pop(q.index(r))
        for i in edges[u]:
            if dist[i[0]] > dist[u] + i[1]:
                # 정점까지의 비용을 갱신할 수 있다면 갱신하기
                dist[i[0]] = dist[u] + i[1]

    return dist

# 변의 리스트(끝점과 비용의 리스트)
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