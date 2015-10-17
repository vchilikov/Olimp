a = list(map(int, input().split()))
print(sum([a[int(ch) - 1] for ch in input()]))
