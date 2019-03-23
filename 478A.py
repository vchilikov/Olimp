c = sum(map(int, input().split()))
print(c // 5 if c % 5 == 0 and c > 0 else -1)