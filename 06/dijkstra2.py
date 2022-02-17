def min_heapify(data, i):
    left = 2 * i + 1
    right = 2 * i + 2
    min = i
    if left < len(data) and data[i][0] > data[left][0]:
        min = left
    if right < len(data) and data[min][0] > data[right][0]:
        min = right
    if min != i:
        data[i], data[min] = data[min], data[i]
        min_heapify(data, min)

def dijkstra(edges, num_v):
    dist = [float('inf')] * num_v
    dist[0] = 0
    q = [[0, 0]]

    while len(q) > 0:
        # 큐에서 최소인 요소를 꺼내기
        q[0], q[-1] = q[-1], q[0]
        _, u = q.pop()
        # 큐를 재구성
        min_heapify(q, 0)
        # 각 변의 비용을 탐색
        for i in edges[u]:
            if dist[i[0]] > dist[u] + i[1]:
                dist[i[0]] = dist[u] + i[1]
                q.append([dist[u] + i[1], i[0]])
                j = len(q) - 1
                while (j > 0) and (q[(j - 1) // 2] > q[j]):
                    q[(j - 1) // 2], q[j] = q[j], q[(j - 1) // 2]
                    j = (j - 1) // 2

    return dist

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