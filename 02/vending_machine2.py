# 거스름돈 금액 구하기
insert_price = input('insert: ')
product_price = input('product: ')
change = int(insert_price) - int(product_price)

# 5,000원 지폐 매수 구하기
r5000 = change // 5000
q5000 = change % 5000
print('5000: ' + str(r5000))

# 1,000원 지폐 매수 구하기
r1000 = q5000 // 1000
q1000 = q5000 % 1000
print('1000: ' + str(r1000))

# 500원 동전 개수 구하기
r500 = q1000 // 500
q500 = q1000 % 500
print('500: ' + str(r500))

# 100원 동전 개수 구하기
r100 = q500 // 100
q100 = q500 % 100
print('100: ' + str(r100))

# 50원 동전 개수 구하기
r50 = q100 // 50
q50 = q100 % 50
print('50: ' + str(r50))

# 10원 동전 개수 구하기
r10 = q50 // 10
q10 = q50 % 10
print('10: ' + str(r10))

# 5원 동전 개수 구하기
r5 = q10 // 5
q5 = q10 % 5
print('5: ' + str(r5))

# 1원 동전 개수 구하기
print('1: ' + str(q5))