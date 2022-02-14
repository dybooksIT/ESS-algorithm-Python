def binary_search(data, value):
    left = 0
    right = len(data) - 1
    while left <= right:
        mid = (left + right) // 2
        if data[mid] == value:
            # 중앙값과 일치하면 위치를 반환
            return mid
        elif data[mid] < value:
            # 중앙값보다 크면 검색 범위의 왼쪽을 바꿈
            left = mid + 1
        else:
            # 중앙값보다 작으면 검색 범위의 오른쪽을 바꿈
            right = mid - 1
    return -1

data = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(binary_search(data, 90))