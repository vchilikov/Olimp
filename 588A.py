n = int(input())
res = 0
last_p = 101
for i in range(n):
    a, p = map(int, input().split())
    if last_p > p:
        last_p = p
    res += a * last_p
print(res)