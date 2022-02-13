# 원주율 π의 근사값을 구하는 함수
# (π는 4 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11 + ... 라는 식으로 구할 수 있음)
def pi(n):
    result = 4
    plus_minus = -1
    for i in range(1, n):
        result += plus_minus * 4 / (i * 2 - 1)
        # 부호를 반전
        plus_minus *= -1

    return result