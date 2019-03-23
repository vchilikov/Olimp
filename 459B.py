n = input()
b = list(map(int, input().split()))
max_b = max(b)
min_b = min(b)
if min_b != max_b:
    print(max_b - min_b, b.count(min_b) * b.count(max_b))
else:
    cnt = b.count(min_b)
    print(0, cnt * (cnt - 1) // 2)
