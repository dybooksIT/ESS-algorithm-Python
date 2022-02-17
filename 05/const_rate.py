import time

data = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]

# 단순히 리스트의 요소를 하나씩 출력
for i in data:
    print(i)

# 리스트의 요소를 하나 출력할 때마다 1초 정지
for i in data:
    print(i)
    time.sleep(1)