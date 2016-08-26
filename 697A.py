t, s, x = map(int, input().split())
print("YES" if (x - t >= 0 and (x - t) % s <= 1) else "NO")
