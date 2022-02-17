data = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]

# 힙 구성
for i in range(len(data)):
    j = i
    while (j > 0) and (data[(j - 1) // 2] < data[j]):
        data[(j - 1) // 2], data[j] = data[j], data[(j - 1) // 2]
        j = (j - 1) // 2

# 정렬 실행
for i in range(len(data), 0, -1):
    # 힙의 맨 앞과 교환
    data[i - 1], data[0] = data[0], data[i - 1]
    j = 0
    while ((2 * j + 1 < i - 1) and (data[j] < data[2 * j + 1])) or ((2 * j + 2 < i - 1) and (data[j] < data[2 * j + 2])):
        if (2 * j + 2 == i - 1) or (data[2 * j + 1] > data[2 * j + 2]):
            # 왼쪽 아래와 교환
            data[j], data[2 * j + 1] = data[2 * j + 1], data[j]
            # 왼쪽 아래로 이동
            j = 2 * j + 1
        else:
            # 오른쪽 아래와 교환
            data[j], data[2 * j + 2] = data[2 * j + 2], data[j]
            # 오른쪽 아래로 이동
            j = 2 * j + 2

print(data)