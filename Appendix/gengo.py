def gengo(year):
    if year < 1868:
        return ''
    elif year < 1912:
        return '明治' + str(year - 1867) + '年'
    elif year < 1926:
        return '大正' + str(year - 1911) + '年'
    elif year < 1989:
        return '昭和' + str(year - 1925) + '年'
    elif year < 2019:
        return '平成' + str(year - 1988) + '年'
    else:
        return '令和' + str(year - 2018) + '年'
