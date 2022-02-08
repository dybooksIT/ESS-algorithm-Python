data = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]

for i in range(len(data)):
    min = i
    for j in range(i + 1, len(data)):
        if data[min] > data[j]:
            min = j

    # 最小値の位置と現在の要素を交換
    data[i], data[min] = data[min], data[i]

print(data)
