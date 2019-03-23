n = int(input())
t = sorted((tuple(map(int, input().split())) for i in range(n)))
last = 0
for el in t:
    last = min(el) if last <= min(el) else max(el)
print(last)