import heapq

def heap_sort(array):
    h = array.copy()
    heapq.heapify(h)
    return [heapq.heappop(h) for _ in range(len(array))]

data = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]
print(heap_sort(data))
