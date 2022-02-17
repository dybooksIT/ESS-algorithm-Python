data = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]

def quick_sort(data):
    if len(data) <= 1:
        return data

    # 피벗으로 리스트의 첫 번째 요소를 사용
    pivot = data[0]

    # 피벗보다 작은 요소로 리스트 만들기
    left = [i for i in data[1:] if i <= pivot]

    # 피벗보다 큰 요소로 리스트 만들기
    right = [i for i in data[1:] if i > pivot]

    left = quick_sort(left)
    right = quick_sort(right)

    # 정렬 결과와 피벗 값을 함께 반환
    return left + [pivot] + right

print(quick_sort(data))