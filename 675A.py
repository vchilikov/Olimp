a, b, c = map(int, input().split())
print("YES" if a == b or (c != 0 and (b - a) % c == 0 and (b - a) // c > 0) else "NO")
