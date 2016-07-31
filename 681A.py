n = int(input())
b = False
for _ in range(n):
    before, after = map(int, input().split()[1:])
    if after > before >= 2400:
        b = True
        break
print("YES" if b else "NO")
