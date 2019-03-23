n, k = map(int, input().split())
a = list(map(int, input().split()))
cnt = 0
for el in a:
    if el > k:
        break
    cnt += 1

for el in a[::-1]:
    if el > k:
        break
    cnt += 1

print(min(cnt, n))
