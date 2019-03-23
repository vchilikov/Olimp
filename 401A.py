n, x = map(int, input().split())
a = abs(sum(map(int, input().split())))
print((a + x - 1) // x)
