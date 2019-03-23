n = int(input())
cnt = 0
for i in range(n):
    p, q = input().split(" ")
    if int(q) - int(p) >= 2:
        cnt += 1
print(cnt)
