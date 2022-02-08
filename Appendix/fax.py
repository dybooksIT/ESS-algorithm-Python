data = '000000111111100111000000001111'

flag = 0
count = 0
result = []
for i in list(data):
    if int(i) == flag:
        count += 1
    else:
        result.append(count)
        count = 1
        flag = 1 - flag

result.append(count)
print(result)
