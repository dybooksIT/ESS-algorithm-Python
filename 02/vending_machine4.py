import sys

input_price = input('insert: ')
if not input_price.isdecimal():
    print('정수를 입력하세요')
    sys.exit()

product_price = input('product: ')
if not product_price.isdecimal():
    print('정수를 입력하세요')
    sys.exit()

change = int(input_price) - int(product_price)

if change < 0:
    print('금액이 부족합니다')
    sys.exit()

coin = [5000, 1000, 500, 100, 50, 10, 5, 1]

for i in coin:
    r = change // i
    change %= i
    print(str(i) + ': ' + str(r))