n = int(input())
a = list(map(int, input().split()))
min_a, max_a = min(a), max(a)
print(max(0, n - a.count(min_a) - a.count(max_a)))
