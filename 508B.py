n = input()
max_n = -1
last_n = int(n[-1])
for i, el in enumerate(n):
    int_el = int(el)
    if int_el % 2 == 0:
        max_n = i
        if int_el < last_n:
            break
print(-1 if max_n == -1 else n[:max_n] + n[-1] + n[max_n + 1: -1] + n[max_n])
