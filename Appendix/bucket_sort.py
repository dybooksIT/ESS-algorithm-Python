data = [9, 4, 5, 2, 8, 3, 7, 8, 3, 2, 6, 5, 7, 9, 2, 9]

# 횟수를 저장할 리스트
result = [0] * 10

for i in data:
    # 횟수를 셈
    result[i] += 1

# 결과 출력
for i in range(10):
    for j in range(result[i]):
        print(i, end=' ')