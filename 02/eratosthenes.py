import math, time

def get_prime(n):
    if n <= 1:
        return []
    prime = [2]
    limit = int(math.sqrt(n))

    # 홀수 리스트 생성
    data = [i + 1 for i in range(2, n, 2)]

    while limit >= data[0]:
        prime.append(data[0])
        # 나누어떨어지지 않은 수만 꺼냄
        data = [j for j in data if j % data[0] != 0]
    return prime + data

print(get_prime(200))

start = time.time()
get_prime(100000)
end = time.time()

print(f"{end - start:.5f} sec")