def chosun(year):
        if year < 1392:
                print('조선시대 전입니다.')
                return ''
        elif year < 1398:
                print('태조 ' + str(year - 1391) + '년')
                return '태조' + str(year - 1391) + '년'
        elif year < 1400:
                return '정종' + str(year - 1397) + '년'
        elif year < 1418:
                return '태종' + str(year - 1399) + '년'
        elif year < 1450:
                return '세종' + str(year - 1417) + '년'
        elif year < 1452:
                return '문종' + str(year - 1449) + '년'
        else:
                return ''

chosun(1394)