import sys

def chosun(year):
    if year < 1392:
        print('조선시대 전입니다.')
    elif year < 1398:
        print('태조 ' + str(year - 1391) + '년')
    elif year < 1400:
        print('정종 ' + str(year - 1397) + '년')
    elif year < 1418:
        print('태종 ' + str(year - 1399) + '년')
    elif year < 1450:
        print('세종 ' + str(year - 1417) + '년')
    elif year < 1452:
        print('문종 ' + str(year - 1449) + '년')
    else:
        print('범위를 벗어났습니다.')

input_year = input('연도 입력: ')

if not input_year.isdecimal():
    print('정수를 입력하세요')
    sys.exit()

change_year = int(input_year)

chosun(change_year)