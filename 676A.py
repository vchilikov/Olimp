n = input()
x, y = (k for k, v in enumerate(input().split()) if v == '1' or v == n)
print(max(y, int(n) - x - 1))
