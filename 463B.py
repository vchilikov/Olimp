n = int(input())
h = [0] + list(map(int, input().split()))
s = 0
res = 0
for i in range(n):
    s += h[i] - h[i + 1]
    if s < 0:
        res += -s
        s = 0
print(res)