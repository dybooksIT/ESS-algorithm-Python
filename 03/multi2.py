n = 10

for i in range(1, n):
    for j in range(1, n):
        for k in range(1, n):
            print(str(i) + '*' + str(j) + '*' + str(k) + \
                '=' + str(i * j * k))
