n = int(input())
a = list(map(int, input().split()))
d = [0] * (max(a) + 1)
for el in a:
    d[el] += el

for i in range(2, len(d)):
    d[i] = max(d[i - 1], d[i - 2] + d[i])
    i += 1

print(d[-1])
