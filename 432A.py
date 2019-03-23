n, k = map(int, input().split())
y = sum(map(lambda x: 5 - k >= int(x), input().split()))
print(y // 3)
