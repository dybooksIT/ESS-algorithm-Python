N = 8

# 대각선 확인
def check(x, col):
    # 배치 완료된 행을 반대 순서로 탐색
    for i, row in enumerate(reversed(col)):
        if (x + i + 1 == row) or (x - i - 1 == row):
            return False
    return True

def search(col):
    if len(col) == N: # 전부 배치되면 출력
        print(col)
        return

    for i in range(N):
        if i not in col: # 동일한 행은 사용하지 않음
            if check(i, col):
                col.append(i)
                search(col)
                col.pop()

search([])