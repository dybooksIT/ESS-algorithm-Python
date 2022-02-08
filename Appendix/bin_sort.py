data = [9, 4, 5, 2, 8, 3, 7, 8, 3, 2, 6, 5, 7, 9, 2, 9]
# 回数を保存するリスト
result = [0] * 10

for i in data:
    # 回数をカウント
    result[i] += 1

# 結果を出力
for i in range(10):
    for j in range(result[i]):
        print(i, end=' ')
