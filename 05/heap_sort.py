data = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]

# ヒープを構成
for i in range(len(data)):
    j = i
    while (j > 0) and (data[(j - 1) // 2] < data[j]):
        data[(j - 1) // 2], data[j] = data[j], data[(j - 1) // 2]
        j = (j - 1) // 2

# ソートを実行
for i in range(len(data), 0, -1):
    # ヒープの先頭と交換
    data[i - 1], data[0] = data[0], data[i - 1]
    j = 0
    while ((2 * j + 1 < i - 1) and (data[j] < data[2 * j + 1]))\
        or ((2 * j + 2 < i - 1) and (data[j] < data[2 * j + 2])):
        if (2 * j + 2 == i - 1) or (data[2 * j + 1] > data[2 * j + 2]):
            # 左下と交換
            data[j], data[2 * j + 1] = data[2 * j + 1], data[j]
            # 左下に移動
            j = 2 * j + 1
        else:
            # 右下と交換
            data[j], data[2 * j + 2] = data[2 * j + 2], data[j]
            # 右下に移動
            j = 2 * j + 2

print(data)
