# 신장과 체중으로 BMI(비만도를 나타내는 체질량 지수)를 구하는 함수
def bmi(height, weight):
    # 신장(cm)의 단위를 m으로 변환
    h = height / 100
    return weight / (h * h)