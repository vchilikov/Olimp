n = int(input())
a = map(int, input().split())
last_act = 0
cnt = 0
for act in a:
    if act == 0:
        last_act = 0
        cnt += 1
    elif act == 3:
        if last_act:
            last_act = 1 if last_act == 2 else 2
    elif act in [1, 2]:
        if last_act == act:
            cnt += 1
            last_act = 0
        else:
            last_act = act

print(cnt)
