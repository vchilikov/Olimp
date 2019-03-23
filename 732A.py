k, r = map(int, input().split())
n = 1
while (k * n) % 10 not in [0, r]:
    n += 1

print(n)