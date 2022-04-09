# 목푯값
goal = 5000000

# 각 도시의 인구
pref = [
    3416918, 2925967, 2453041, 1525849, 1496172, 1193894, 1147037, 
    1068641, 1061440, 1044579, 942649, 840047, 828947, 818760, 
    702545, 654963, 652845, 650599, 565392, 542713, 521642, 
    506494, 489202
]

# 500만 명에 가까운 인구 수
min_total = 0

# 두 지역의 인구 수를 저장하는 임시 변수
local_temp = 0

# 지역 1~3 인구 수의 인덱스를 저장
local_index1 = 0
local_index2 = 0
local_index3 = 0

def search(total, pos):
    global min_total, local_temp, local_index1, local_index2, local_index3
    if pos >= len(pref):
        return
    if total < goal:
        if abs(goal - (total + pref[pos])) < abs(goal - min_total):
            min_total = total + pref[pos]
            local_temp = total
            local_index1 = pos
        search(total + pref[pos], pos + 1)
        search(total, pos + 1)

    for local_index2 in range(22):
        for local_index3 in range(22):
            if local_temp - pref[local_index2] == pref[local_index3]:
                break
        break

search(0, 0)
print(min_total)
print(pref[local_index1])
print(pref[local_index2])
print(pref[local_index3])