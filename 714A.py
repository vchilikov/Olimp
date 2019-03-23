inp = list(map(int, input().split()))
l = max(inp[0], inp[2])
r = min(inp[1], inp[3])
print(max(r - l + 1, 0) - (l <= inp[4] <= r))
