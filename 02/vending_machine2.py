# お釣りの金額を求める
insert_price = input('insert: ')
product_price = input('product: ')
change = int(insert_price) - int(product_price)

# 5000円札の枚数を求める
r5000 = change // 5000
q5000 = change % 5000
print('5000: ' + str(r5000))

# 1000円札の枚数を求める
r1000 = q5000 // 1000
q1000 = q5000 % 1000
print('1000: ' + str(r1000))

# 500円玉の枚数を求める
r500 = q1000 // 500
q500 = q1000 % 500
print('500: ' + str(r500))

# 100円玉の枚数を求める
r100 = q500 // 100
q100 = q500 % 100
print('100: ' + str(r100))

# 50円玉の枚数を求める
r50 = q100 // 50
q50 = q100 % 50
print('50: ' + str(r50))

# 10円玉の枚数を求める
r10 = q50 // 10
q10 = q50 % 10
print('10: ' + str(r10))

# 5円玉の枚数を求める
r5 = q10 // 5
q5 = q10 % 5
print('5: ' + str(r5))

# 1円玉の枚数を求める
print('1: ' + str(q5))
