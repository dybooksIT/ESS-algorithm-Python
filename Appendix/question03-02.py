# 원주율 π의 근사값을 구하는 함수
# (n×n의 정사각형 중, 부채꼴 범위에 들어가는 수를 셈)
def pi(n):
    cnt = 0
    for i in range(n):
        for j in range(n):
            # 피타고라스 정리  (Pythagoras's theorem)로 부채꼴 내부인지 판정
            if i * i + j * j <= n * n:
                cnt += 1
    # 부채꼴에서 원형으로 변환하기 위해 4배로 함
    return cnt * 4 / (n * n)