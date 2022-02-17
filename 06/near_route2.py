import functools

M, N = 6, 5

# 파이썬에서는 아래 1행만 추가하면 재귀 처리를 메모이제이션(memoization)할 수 있음
@functools.lru_cache(maxsize = None)
def search(m, n):
    if (m == 0) or (n == 0):
        return 1

    return search(m - 1, n) + search(m, n - 1)

print(search(M, N))