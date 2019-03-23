a, b, s = map(lambda x: abs(int(x)), input().split())
print("Yes" if a + b <= s and (s - a - b) % 2 == 0 else "No")