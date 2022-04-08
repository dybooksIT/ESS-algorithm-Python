import heapq

def dijkstra(edges, num_v, goal):
    dist = [float('inf')] * num_v
    dist[0] = 0
    q = []
    heapq.heappush(q, [0, [0]])

    while len(q) > 0:
        # 힙에서 요소 꺼내기
        _, u = heapq.heappop(q)
        last = u[-1]

        if last == goal:
            return u
        for i in edges[last]:
            if dist[i[0]] > dist[last] + i[1]:
                # 정점까지의 비용을 갱신할 수 있다면 갱신해 힙에 등록
                dist[i[0]] = dist[last] + i[1]
                heapq.heappush(q, [dist[last] + i[1], u + [i[0]]])
    return []

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

print(dijkstra(edges, 7, 6))