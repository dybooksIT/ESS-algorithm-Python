# 목푯값
goal = 5000000

# 각 도시의 인구
pref = [
    3416918, 2925967, 2453041, 1525849, 1496172, 1193894, 1147037, 
    1068641, 1061440, 1044579, 942649, 840047, 828947, 818760, 
    702545, 654963, 652845, 650599, 565392, 542713, 521642, 
    506494, 489202
]

min_total = 0
def search(total, pos):
    global min_total
    if pos >= len(pref):
        return
    if total < goal:
        if abs(goal - (total + pref[pos])) < abs(goal - min_total):
            min_total = total + pref[pos]
        search(total + pref[pos], pos + 1)
        search(total, pos + 1)

search(0, 0)
print(min_total)