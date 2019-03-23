n = int(input())
t = list(map(int, input().split()))
p = m = f = cnt = 0
w = ""
while p < n and m < n and f < n:
    while p < n and t[p] != 1:
        p += 1
    while m < n and t[m] != 2:
        m += 1
    while f < n and t[f] != 3:
        f += 1
    if p < n and m < n and f < n:
        w += str(p + 1) + " " + str(m + 1) + " " + str(f + 1) + "\n"
        cnt += 1
        p += 1
        m += 1
        f += 1

print(cnt)
print(w)
